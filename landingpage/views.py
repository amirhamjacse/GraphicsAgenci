from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages


class IndexView(View):
    template = "index6.html"
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

        #about section
        'about': About.objects.first(),
        
        # Projects
        'featured_projects': Project.objects.filter(is_featured=True)[:4],
        'all_projects': Project.objects.all().order_by('-created_at'),

        # moveable logo
        'moveable_logo': MoveableLogo.objects.filter(is_active=True),
        
        # Services
        'featured_services': Service.objects.filter(is_featured=True)[:6],
        'all_services': Service.objects.all().order_by('order'),
        
        # Case Studies
        'case_studies': BrandingCaseStudy.objects.filter(is_active=True)[:4],
        
        # Testimonials
        'testimonials': Testimonial.objects.filter(is_featured=True),
        
        # Team
        'team_members': TeamMember.objects.filter(is_active=True).order_by('order'),
        
        # Contact Info
        'contact_email': SiteSetting.objects.first().contact_email,
        'contact_phone': SiteSetting.objects.first().contact_phone
    }
    # a = MoveableLogo.objects.all()
    # print(a, "-----------------")
    return render(request, 'index6.html', context)

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

            #about section
            'about': About.objects.first(),

            # Projects
            'featured_projects': Project.objects.filter(is_featured=True)[:4],
            'all_projects': Project.objects.all().order_by('-created_at'),

            # Services
            'featured_services': Service.objects.filter(is_featured=True)[:6],
            'all_services': Service.objects.all().order_by('order'),

            # moveable_logo
            'moveable_logo': MoveableLogo.objects.filter(is_active=True),
        

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


def contact_us_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')  # New phone field
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            attachment = request.FILES.get('attachment')

            # Validate file size (10 MB max)
            if attachment and attachment.size > 10 * 1024 * 1024:  # 10 MB
                messages.error(request, "File size cannot exceed 10 MB.")
                return redirect('index')  # Change 'land' to your redirect page name

            # Create contact submission
            ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message,
                attachment=attachment
            )

            messages.success(request, "Your message has been sent successfully!Thank you")
            return redirect('index')  # Replace 'land' with your success URL name

        except Exception as e:
            messages.error(request, f"Something went wrong: {e}")
            # You can log the error for debugging purposes

    return render(request, 'index3.html')