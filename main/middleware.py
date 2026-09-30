"""Keeps per-page SEO tags consistent without repeating them in every template.

For each HTML page it (1) copies the page <title> and meta description into the Open Graph and
Twitter tags, (2) makes social image URLs absolute, and (3) adds BreadcrumbList JSON-LD when the
page has none of its own.
"""
import html
import json
import re

SITE = 'https://trendcrafters.global'

_TITLE = re.compile(r'<title>(.*?)</title>', re.S)
_DESC = re.compile(r'<meta name="description" content="(.*?)"', re.S)

CRUMBS = {
    'about': 'About', 'services': 'Services', 'work': 'Our Work', 'contact': 'Contact', 'clients': 'Our Clients',
    'team': 'Our Team', 'maintenance': 'Website Maintenance', 'photo_shoot': 'Photography',
    'web-development': 'Web Development', 'web-app-development': 'Web App Development',
    'digital-marketing': 'Digital Marketing', 'brand-campaign': 'Branding & Campaigns', 'production': 'Production',
    'it-solutions': 'IT Solutions',
}


def _breadcrumb(path, title):
    parts = [p for p in path.strip('/').split('/') if p]
    if not parts:
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'}]
    url = ''
    for i, p in enumerate(parts, start=2):
        url += '/' + p
        name = CRUMBS.get(p) or (title.split('|')[0].strip() if i == len(parts) + 1 else p.replace('-', ' ').title())
        items.append({"@type": "ListItem", "position": i, "name": name, "item": SITE + url + '/'})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def _set(body, pattern, value):
    return re.sub(pattern, lambda m: m.group(1) + html.escape(value, quote=True) + m.group(2), body, count=1)


class SeoSyncMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 200 or 'text/html' not in response.get('Content-Type', ''):
            return response
        body = response.content.decode(response.charset or 'utf-8')
        t, d = _TITLE.search(body), _DESC.search(body)
        if not (t and d):
            return response
        title, desc = html.unescape(t.group(1).strip()), html.unescape(d.group(1).strip())
        for prop in ('og:title', 'twitter:title'):
            body = _set(body, r'(<meta (?:property|name)="%s" content=")[^"]*(")' % prop, title)
        for prop in ('og:description', 'twitter:description'):
            body = _set(body, r'(<meta (?:property|name)="%s" content=")[^"]*(")' % prop, desc)
        # absolute social images
        body = re.sub(r'(<meta (?:property="og:image"|name="twitter:image"|name="image") content=")(/[^"]*)(")',
                      lambda m: m.group(1) + SITE + m.group(2) + m.group(3), body)
        if 'BreadcrumbList' not in body:
            ld = _breadcrumb(request.path, title)
            if ld:
                body = body.replace('</head>', '<script type="application/ld+json">' + json.dumps(ld) + '</script>\n</head>', 1)
        response.content = body.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))
        return response
