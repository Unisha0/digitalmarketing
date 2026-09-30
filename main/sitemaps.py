import functools
import html
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from django.contrib.sitemaps import Sitemap
from django.test import Client
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent
SITE = 'https://trendcrafters.global'
_IMG = re.compile(r'<img[^>]+?src="([^"]+)"[^>]*>', re.S)
_ALT = re.compile(r'alt="([^"]*)"')
_SKIP = ('favicon', 'logo', 'og-image', '.svg', 'data:')

# view name -> templates that make up the page (used for an accurate <lastmod>)
_TEMPLATE_DIR = BASE_DIR / 'main' / 'templates' / 'main'


def _page_templates(name):
    candidates = {
        'index': ['index.html'], 'about': ['about.html'], 'services': ['services.html'], 'work': ['work.html'],
        'contact': ['contact.html'], 'photo_shoot': ['photo_shoot.html'], 'production': ['production.html'],
        'pr_video': ['pr/video.html'], 'pr_ads': ['pr/ads.html'], 'it_solutions': ['it/hub.html'],
        'digital_marketing': ['digital_marketing.html'], 'dm_social_media': ['dm/social_media.html'],
        'dm_meta_ads': ['dm/meta_ads.html'], 'dm_tiktok': ['dm/tiktok.html'],
        'dm_content_reels': ['dm/content_reels.html'], 'dm_seo': ['dm/seo.html'],
        'dm_community': ['dm/community.html'], 'brand_campaign': ['brand_campaign.html'],
        'br_identity': ['br/identity.html'], 'br_campaigns': ['br/campaigns.html'],
        'br_graphic': ['br/graphic_design.html'], 'br_story': ['br/storytelling.html'],
        'web_development': ['web_development.html'], 'web_app_development': ['web_app_development.html'],
        'maintenance': ['maintenance.html'], 'partners': ['partners.html'], 'team': ['team.html'],
    }
    return [_TEMPLATE_DIR / t for t in candidates.get(name, [])]


@functools.lru_cache(maxsize=None)
def _lastmod(name):
    """Newest change to the page's template: git commit date when available, else file mtime."""
    best = None
    for path in _page_templates(name) + [_TEMPLATE_DIR / 'base.html'][:0]:
        if not path.exists():
            continue
        try:
            out = subprocess.run(['git', 'log', '-1', '--format=%cI', '--', str(path)], cwd=BASE_DIR,
                                 capture_output=True, text=True, timeout=5).stdout.strip()
            dt = datetime.fromisoformat(out) if out else None
        except Exception:
            dt = None
        if dt is None:
            dt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        best = max(best, dt) if best else dt
    return best


@functools.lru_cache(maxsize=None)
def _images(url):
    """Own-site photos shown on the page, for the image sitemap (first 12, de-duplicated)."""
    try:
        page = Client(HTTP_HOST='trendcrafters.global', secure=True).get(url).content.decode('utf-8', 'ignore')
    except Exception:
        return []
    seen, out = set(), []
    for m in _IMG.finditer(page):
        src = m.group(1)
        if not src.startswith('/static/') or any(k in src.lower() for k in _SKIP) or src in seen:
            continue
        seen.add(src)
        alt = _ALT.search(m.group(0))
        out.append({'loc': SITE + src, 'title': html.unescape(alt.group(1)) if alt and alt.group(1) else ''})
        if len(out) >= 12:
            break
    return out


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    protocol = 'https'
    HIGH = {'index': 1.0, 'digital_marketing': 0.9, 'brand_campaign': 0.9, 'production': 0.9, 'it_solutions': 0.9,
            'dm_social_media': 0.9, 'contact': 0.8, 'work': 0.8, 'about': 0.8, 'services': 0.8}

    def priority(self, item):
        return self.HIGH.get(item, 0.7)

    def items(self):
        # list the view names for static/important pages
        return [
            'index',
            'about',
            'services',
            'work',
            'contact',
            'photo_shoot',
            'production',
            'pr_video',
            'pr_ads',
            'it_solutions',
            'digital_marketing',
            'dm_social_media',
            'dm_meta_ads',
            'dm_tiktok',
            'dm_content_reels',
            'dm_seo',
            'dm_community',
            'brand_campaign',
            'br_identity',
            'br_campaigns',
            'br_graphic',
            'br_story',
            'web_development',
            'web_app_development',
            'maintenance',
            'partners',
            'team',
        ]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return _lastmod(item)

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(page=page, site=site, protocol=protocol)
        for u in urls:
            path = reverse(u['item'])
            u['location'] = SITE + path            # always the canonical host, never the request host
            u['images'] = _images(path)
            u['lastmod_iso'] = u['lastmod'].isoformat(timespec='seconds') if u.get('lastmod') else ''
        return urls
