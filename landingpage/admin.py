from django.contrib import admin
from .models import (Project, Service, BrandingCaseStudy, 
                    Testimonial, TeamMember, ContactSubmission,
                    SiteSetting, HomeSection)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_featured')
    list_editable = ('order', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BrandingCaseStudy)
class BrandingCaseStudyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'is_featured', 'created_at')
    list_filter = ('is_featured',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email', 'subject')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'title', 'is_active', 'order')
    list_editable = ('is_active', 'order')