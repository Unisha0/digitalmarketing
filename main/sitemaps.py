from django.contrib.sitemaps import Sitemap
from django.urls import reverse


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
