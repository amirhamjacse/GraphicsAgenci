from django.contrib import admin
from .models import (Project, Service, BrandingCaseStudy, 
                    Testimonial, TeamMember, ContactSubmission,
                    SiteSetting, HomeSection,
                    MoveableLogo,
                    ProjectSection)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project_type',
        'is_featured',
        'created_at'
        )
    list_filter = (
        'is_featured',
        'created_at'
        )
    search_fields = (
        'title',
        'description'
        )
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

@admin.register(MoveableLogo)
class Moveablelogoadmin(admin.ModelAdmin):
    list_display = (
        'name',
        'detail',
        'icon',
        'order',
        'is_active',
        'created_at',
    )


from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'updated_at')  # Columns in admin list view
    search_fields = ('title', 'subtitle')  # Searchable fields
    list_filter = ('created_at', 'updated_at')  # Filter sidebar
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only

    fieldsets = (
        ('About Content', {
            'fields': ('title', 'subtitle', 'description', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


from .models import BrandingCaseStudy, BrandingCaseStudySection

class BrandingCaseStudySectionInline(admin.TabularInline):
    model = BrandingCaseStudySection
    extra = 1

# @admin.register(BrandingCaseStudy)
# class BrandingCaseStudyAdmin(admin.ModelAdmin):
#     inlines = [BrandingCaseStudySectionInline]
#     list_display = ['name', 'is_active', 'created_at']

class BrandingCaseStudySectionInline(admin.StackedInline):  # or TabularInline for a simpler table-style layout
    model = BrandingCaseStudySection
    extra = 1  # How many empty forms to show
    fields = ['title', 'image', 'description', 'order']
    ordering = ['order']

@admin.register(BrandingCaseStudySection)
class BrandingCaseStudySectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'case_study', 'order']
    list_filter = ['case_study']
    search_fields = ['title', 'description']
    ordering = ['case_study', 'order']

# admin.py
from django.contrib import admin
from .models import ProjectSection

from django.contrib import admin
from .models import ProjectSection

@admin.register(ProjectSection)
class ProjectSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")  # fields that actually exist
    search_fields = ("title", "description")       # searchable fields
