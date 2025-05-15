from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404



class IndexView(View):
    template = "index.html"
    def get(self, request):
        return render(request, self.template)


from django.shortcuts import render
from .models import *

def index(request):
    context = {
        # Site Settings
        'site_settings': SiteSetting.objects.first(),
        
        # Home Sections
        'home_sections': HomeSection.objects.filter(is_active=True).order_by('order'),
        
        # Projects
        'featured_projects': Project.objects.filter(is_featured=True)[:4],
        'all_projects': Project.objects.all().order_by('-created_at'),
        
        # Services
        'featured_services': Service.objects.filter(is_featured=True)[:6],
        'all_services': Service.objects.all().order_by('order'),
        
        # Case Studies
        'case_studies': BrandingCaseStudy.objects.filter(is_active=True)[:3],
        
        # Testimonials
        'testimonials': Testimonial.objects.filter(is_featured=True),
        
        # Team
        'team_members': TeamMember.objects.filter(is_active=True).order_by('order'),
        
        # Contact Info
        'contact_email': SiteSetting.objects.first().contact_email,
        'contact_phone': SiteSetting.objects.first().contact_phone
    }
    return render(request, 'index.html', context)

from django.views import View
from django.shortcuts import render

class LandPageView(View):
    def get(self, request, *args, **kwargs):
        # site_settings = SiteSetting.objects.all()
        site_settings = get_object_or_404(SiteSetting)

        context = {
            # Site Settings
            'site_settings': site_settings,

            # Home Sections
            'home_sections': HomeSection.objects.filter(is_active=True).order_by('order'),

            # Projects
            'featured_projects': Project.objects.filter(is_featured=True)[:4],
            'all_projects': Project.objects.all().order_by('-created_at'),

            # Services
            'featured_services': Service.objects.filter(is_featured=True)[:6],
            'all_services': Service.objects.all().order_by('order'),

            # Case Studies
            'case_studies': BrandingCaseStudy.objects.filter(is_active=True)[:3],

            # Testimonials
            'testimonials': Testimonial.objects.filter(is_featured=True),

            # Team
            'team_members': TeamMember.objects.filter(is_active=True).order_by('order'),

            # Contact Info (from site settings)
            'contact_email': site_settings.contact_email if site_settings else '-',
            'contact_phone': site_settings.contact_phone if site_settings else '-',
        }

        return render(request, 'index3.html', context)
