from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

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
