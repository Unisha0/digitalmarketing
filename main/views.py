from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from functools import wraps
import time

def rate_limit(key_prefix, limit=20, period=60):
    """
    Rate limiting decorator that allows X requests per Y seconds
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            key = f"{key_prefix}:{request.META.get('REMOTE_ADDR', '')}"
            requests = cache.get(key, [])
            now = time.time()
            
            # Filter out old requests
            requests = [req for req in requests if req > now - period]
            
            if len(requests) >= limit:
                return HttpResponse("Too many requests. Please try again later.", status=429)
            
            requests.append(now)
            cache.set(key, requests, timeout=period)
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

GOOGLE_REVIEW_URL = "https://share.google/1RULRy1xx4IW62x6F"

# Paste REAL Google reviews here (copy the reviewer's name and text from the Google listing).
# "photo" is optional: a file under static/main/images/reviews/ (e.g. "reviews/ram.jpg");
# without one, a gradient initial is shown.
GOOGLE_REVIEWS = [
    # {"name": "Reviewer Name", "rating": 5, "text": "Review text...", "date": "2 months ago", "photo": ""},
]


def index(request):
    return render(request, 'main/index.html', {
        'google_review_url': GOOGLE_REVIEW_URL,
        'google_reviews': GOOGLE_REVIEWS,
        'clients': CLIENTS,
        'featured_clients': [c for c in CLIENTS if c.get('logo')][:12],
    })  # homepage template

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

@rate_limit('contact', limit=20, period=60)  # 20 requests per minute
@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            message = request.POST.get('message', '').strip()
            service = request.POST.get('service', '').strip()[:60]

            # Validation
            if not all([name, email, message]):
                messages.error(request, "Please fill in all required fields.")
                return redirect('contact')

            # Email validation
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "Please enter a valid email address.")
                return redirect('contact')

            # Phone validation (optional field)
            if phone:
                phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
                if not phone_pattern.match(phone):
                    messages.error(request, "Please enter a valid phone number.")
                    return redirect('contact')

            # Message length validation
            if len(message) < 10:
                messages.error(request, "Message is too short. Please provide more details.")
                return redirect('contact')

            # Prepare email with IP address for tracking
            ip_address = request.META.get('REMOTE_ADDR', 'Unknown')
            user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
            
            full_message = (
                f"New Contact Form Submission\n"
                f"------------------------\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Interested in: {service}\n"
                f"Message: {message}\n\n"
                f"Additional Information:\n"
                f"IP Address: {ip_address}\n"
                f"User Agent: {user_agent}\n"
                f"------------------------"
            )

            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=full_message,
                    from_email=email,
                    recipient_list=['trendcraftersglobal@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "Thank you for your message! We'll get back to you soon.")
            except Exception as e:
                messages.error(request, "There was an error sending your message. Please try again later.")
                # Log the error here if you have logging configured
                print(f"Email error: {str(e)}")  # Replace with proper logging
                
            return redirect('contact')

        except Exception as e:
            messages.error(request, "An unexpected error occurred. Please try again later.")
            # Log the error here
            print(f"Unexpected error: {str(e)}")  # Replace with proper logging
            return redirect('contact')

    return render(request, 'main/contact.html')


def about(request):
    return _ab_page(request, 'main/about.html', 'about')

def services(request):
    return render(request, 'main/services.html')

from .clients import CLIENTS


def work(request):
    return render(request, 'main/work.html', {'clients': CLIENTS})

def brand_campaign(request):
    return _br_page(request, 'main/brand_campaign.html', 'hub')

# Branding sub-pages: each has its own template and layout under main/br/
def br_identity(request):
    return _br_page(request, 'main/br/identity.html', 'identity')

def br_campaigns(request):
    return _br_page(request, 'main/br/campaigns.html', 'campaigns')

def br_graphic(request):
    return _br_page(request, 'main/br/graphic_design.html', 'graphic')

def br_story(request):
    return _br_page(request, 'main/br/storytelling.html', 'story')

import json
from django.urls import reverse
from .clients import CLIENTS
from .seo_data import DM_PAGES, BR_PAGES, PR_PAGES, IT_PAGES, AB_PAGES


def _section_page(request, template, page, is_hub, parent_name, parent_url_name, extra=None):
    """Render a service page with its keywords, FAQs and JSON-LD schema (FAQPage, Service, BreadcrumbList)."""
    base = f"{request.scheme}://{request.get_host()}"
    schema = [
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faqs"]]},
        {"@context": "https://schema.org", "@type": "Service", "name": page["name"],
         "serviceType": page["name"], "provider": {"@id": "https://trendcrafters.global/#organization"},
         "areaServed": ["Nepal", "Kathmandu", "Lalitpur", "Bhaktapur"],
         "url": base + reverse(page["url_name"])},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": parent_name, "item": base + reverse(parent_url_name)},
        ] + ([] if is_hub else [
            {"@type": "ListItem", "position": 3, "name": page["name"], "item": base + reverse(page["url_name"])}])},
    ]
    ctx = {"dm": page, "dm_schema": json.dumps(schema, ensure_ascii=False)}
    ctx.update(extra or {})
    return render(request, template, ctx)


def _dm_page(request, template, key):
    return _section_page(request, template, DM_PAGES[key], key == "hub", "Digital Marketing", "digital_marketing")


def _pr_page(request, template, key):
    return _section_page(request, template, PR_PAGES[key], key == "hub", "Production Services", "production")


def _it_page(request, template, key):
    return _section_page(request, template, IT_PAGES[key], key == "hub", "IT Solutions", "it_solutions")


def _ab_page(request, template, key, extra=None):
    return _section_page(request, template, AB_PAGES[key], True, "About Us", "about", extra)


def _br_page(request, template, key):
    return _section_page(request, template, BR_PAGES[key], key == "hub", "Branding & Campaigns", "brand_campaign")


def digital_marketing(request):
    return _dm_page(request, 'main/digital_marketing.html', 'hub')

# Digital marketing sub-pages: each has its own template and layout under main/dm/
def dm_social_media(request):
    return _dm_page(request, 'main/dm/social_media.html', 'social')

def dm_meta_ads(request):
    return _dm_page(request, 'main/dm/meta_ads.html', 'meta')

def dm_tiktok(request):
    return _dm_page(request, 'main/dm/tiktok.html', 'tiktok')

def dm_content_reels(request):
    return _dm_page(request, 'main/dm/content_reels.html', 'content')

def dm_seo(request):
    return _dm_page(request, 'main/dm/seo.html', 'seo')

def dm_community(request):
    return _dm_page(request, 'main/dm/community.html', 'community')

def pr_video(request):
    return _pr_page(request, 'main/pr/video.html', 'video')

def pr_ads(request):
    return _pr_page(request, 'main/pr/ads.html', 'ads')

def it_solutions(request):
    return _it_page(request, 'main/it/hub.html', 'hub')

def photo_shoot(request):
    return _pr_page(request, 'main/photo_shoot.html', 'photo')

def production(request):
    return _pr_page(request, 'main/production.html', 'hub')

def web_development(request):
    return _it_page(request, 'main/web_development.html', 'web')

def web_app_development(request):
    return _it_page(request, 'main/web_app_development.html', 'app')

def maintenance(request):
    return _it_page(request, 'main/maintenance.html', 'maint')

def partners(request):
    """Our Clients page (URL name kept as 'partners' so existing links keep working)."""
    return _ab_page(request, 'main/partners.html', 'partners', extra={'clients': CLIENTS})


# Team members shown on /team/. Edit roles/bios here; add a photo by setting
# "photo" to a file under static/main/images/team/ (e.g. "team/jenisha.jpg").
TEAM_MEMBERS = [
    {"name": "Saksham Karki", "role": "Founder & CEO", "photo": "home/team-founder.jpg",
     "bio": "Leads Trend Crafters from our Tinkune Sahyoginagar, Kathmandu studio, pairing local market insight with international creative standards.",
     "linkedin": "", "featured": True},
    {"name": "Jenisha Chaulagain", "role": "Project Manager", "photo": "", "bio": "",
     "linkedin": "https://www.linkedin.com/in/jenisha-chaulagain-7423232ba/"},
    {"name": "Devashish Shrestha", "role": "Marketing Head", "photo": "", "bio": "",
     "linkedin": "https://www.linkedin.com/in/devashishshresthaofficial/"},
    {"name": "Divyam Koirala", "role": "Social Media Manager", "photo": "", "bio": "",
     "linkedin": "https://www.linkedin.com/in/divyam-koirala-853922378/"},
    {"name": "Dipankar Tamrakar", "role": "Editor", "photo": "", "bio": "", "linkedin": ""},
    {"name": "Sumit Mishra", "role": "Graphic Designer", "photo": "", "bio": "", "linkedin": ""},
]


def team(request):
    return render(request, 'main/team.html', {'members': TEAM_MEMBERS})
