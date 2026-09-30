from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponse
from . import views

urlpatterns = [
    # Google Search Console ownership verification
    path('googlecf3f0f13be39c99d.html', lambda request: HttpResponse('google-site-verification: googlecf3f0f13be39c99d.html', content_type='text/html'), name='google_verify'),
    path('health/', lambda request: HttpResponse('ok', content_type='text/plain'), name='health'),
    path('', views.index, name='index'),         # Landing page
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),  # Contact page
    path('brand-campaign/', views.brand_campaign, name='brand_campaign'),
    path('brand-campaign/brand-identity/', views.br_identity, name='br_identity'),
    path('brand-campaign/brand-campaigns/', views.br_campaigns, name='br_campaigns'),
    path('brand-campaign/graphic-design/', views.br_graphic, name='br_graphic'),
    path('brand-campaign/brand-storytelling/', views.br_story, name='br_story'),
    path('digital-marketing/', views.digital_marketing, name='digital_marketing'),
    path('digital-marketing/social-media-marketing/', views.dm_social_media, name='dm_social_media'),
    path('digital-marketing/meta-ads/', views.dm_meta_ads, name='dm_meta_ads'),
    path('digital-marketing/tiktok-marketing/', views.dm_tiktok, name='dm_tiktok'),
    path('digital-marketing/content-reels-strategy/', views.dm_content_reels, name='dm_content_reels'),
    path('digital-marketing/seo/', views.dm_seo, name='dm_seo'),
    path('digital-marketing/community-management/', views.dm_community, name='dm_community'),
    path('photo_shoot/', views.photo_shoot, name='photo_shoot'),
    path('production/', views.production, name='production'),
    path('production/video-reels/', views.pr_video, name='pr_video'),
    path('production/commercial-ads/', views.pr_ads, name='pr_ads'),
    path('it-solutions/', views.it_solutions, name='it_solutions'),
    path('web-development/', views.web_development, name='web_development'),
    path('web-app-development/', views.web_app_development, name='web_app_development'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('clients/', views.partners, name='partners'),
    path('partners/', RedirectView.as_view(pattern_name='partners', permanent=True)),
    path('team/', views.team, name='team'),
]
