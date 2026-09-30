"""Keeps per-page SEO tags consistent without repeating them in every template.

For each HTML page it (1) copies the page <title> and meta description into the Open Graph and
Twitter tags, (2) makes social image URLs absolute, and (3) adds BreadcrumbList JSON-LD when the
page has none of its own.
"""
import html
import json
import re
import struct
from functools import lru_cache

from django.conf import settings
from django.contrib.staticfiles import finders

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


_IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)


def _read_size(path):
    """(width, height) from a PNG/JPEG/GIF/WebP header, or None."""
    try:
        with open(path, 'rb') as f:
            head = f.read(32)
            if head[:8] == b'\x89PNG\r\n\x1a\n':
                return struct.unpack('>II', head[16:24])
            if head[:6] in (b'GIF87a', b'GIF89a'):
                return struct.unpack('<HH', head[6:10])
            if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
                if head[12:16] == b'VP8 ':
                    w, h = struct.unpack('<HH', head[26:30]); return w & 0x3FFF, h & 0x3FFF
                if head[12:16] == b'VP8L':
                    b = struct.unpack('<I', head[21:25])[0]; return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
                if head[12:16] == b'VP8X':
                    return int.from_bytes(head[24:27], 'little') + 1, int.from_bytes(head[27:30], 'little') + 1
            if head[:2] == b'\xff\xd8':
                f.seek(2)
                while True:
                    marker = f.read(2)
                    if len(marker) < 2 or marker[0] != 0xFF:
                        return None
                    if marker[1] in (0xC0, 0xC1, 0xC2):
                        f.read(3); h, w = struct.unpack('>HH', f.read(4)); return w, h
                    seglen = struct.unpack('>H', f.read(2))[0]
                    f.seek(seglen - 2, 1)
    except Exception:
        return None
    return None


@lru_cache(maxsize=None)
def _static_size(url_path):
    rel = url_path[len(settings.STATIC_URL):]
    found = finders.find(rel) if settings.DEBUG else None
    path = found or str(settings.STATIC_ROOT / rel)
    return _read_size(path)


def _add_dimensions(body):
    """Declare width/height on <img> tags that lack them, so the browser reserves space (less layout shift)."""
    def fix(m):
        tag = m.group(0)
        if re.search(r'\swidth=', tag, re.I) or re.search(r'\sheight=', tag, re.I):
            return tag
        src = re.search(r'\ssrc="([^"?#]+)', tag)
        if not src or not src.group(1).startswith(settings.STATIC_URL):
            return tag
        size = _static_size(src.group(1))
        if not size:
            return tag
        end = '/>' if tag.endswith('/>') else '>'
        return tag[:-len(end)].rstrip() + f' width="{size[0]}" height="{size[1]}"' + end
    return _IMG_TAG.sub(fix, body)


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
        body = _add_dimensions(body)
        response.content = body.encode(response.charset or 'utf-8')
        if response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))
        return response
