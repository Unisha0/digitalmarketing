from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # Landing page
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),  # Contact page
    path('brand-campaign/', views.brand_campaign, name='brand_campaign'),
    path('digital-marketing/', views.digital_marketing, name='digital_marketing'),
    path('photo_shoot/', views.photo_shoot, name='photo_shoot'),
    path('production/', views.production, name='production'),
    path('web-development/', views.web_development, name='web_development'),
    path('web-app-development/', views.web_app_development, name='web_app_development'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('partners/', views.partners, name='partners'),
    path('team/', views.team, name='team'),
]
