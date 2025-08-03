from django.db import models
from django.core.validators import URLValidator
from django.utils.text import slugify
from django_resized import ResizedImageField  # Requires django-resized package


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    project_type = models.CharField(max_length=100, blank=True)  # e.g., "Animated, portfolio"
    thumbnail = ResizedImageField(size=[800, 600], upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # Or use an ImageField for icons
    logo = ResizedImageField(size=[300, 200], upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class BrandingCaseStudy(models.Model):
    name = models.CharField(max_length=100)
    logo = ResizedImageField(size=[300, 200], upload_to='case_studies/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Branding Case Studies"
        ordering = ['-created_at']


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100, blank=True)
    client_company = models.CharField(max_length=100, blank=True)
    client_photo = ResizedImageField(size=[200, 200], upload_to='testimonials/', blank=True, null=True)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.client_company}"

    class Meta:
        ordering = ['-created_at']


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = ResizedImageField(size=[400, 400], upload_to='team/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    facebook_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Facebook Profile"
    )
    twitter_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Twitter Profile"
    )
    linkedin_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="LinkedIn Profile"
    )
    instagram_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Instagram Profile"
    )
    github_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="GitHub Profile"
    )

    # social_links = models.JSONField(default=dict, blank=True)  # Stores social media links as JSON

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        ordering = ['order']


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Include country code, e.g. +1 234 567 890")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    attachment = models.FileField(upload_to='contact_attachments/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-submitted_at']


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="DesignClock")
    logo = ResizedImageField(size=[300, 100], upload_to='site/', blank=True, null=True)
    footer_description = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    # social_links = models.JSONField(default=dict, blank=True)  # Stores social media links as JSON
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True)
    hero_image = ResizedImageField(size=[1600, 900], upload_to='hero/', blank=True, null=True)
    cta_button_text = models.CharField(max_length=50, default="Contact Us")
    facebook_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Facebook Profile"
    )
    twitter_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Twitter Profile"
    )
    linkedin_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="LinkedIn Profile"
    )
    instagram_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Instagram Profile"
    )
    github_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="GitHub Profile"
    )
    dribble_url = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Dribble Profile"
    )


    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"


class MoveableLogo(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=20)
    icon = ResizedImageField(
        size=[200, 200],
        upload_to='mvicons/',
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HomeSection(models.Model):
    SECTION_CHOICES = [
        ('projects', 'Projects View'),
        ('services', 'Our Services'),
        ('case_studies', 'Branding Case Study'),
        ('testimonials', 'Testimonials'),
    ]
    
    section_type = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_section_type_display()

    class Meta:
        ordering = ['order']


# class BrandingCaseStudy(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='branding_case_studies/')
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         verbose_name_plural = "Branding Case Studies"
#         ordering = ['-created_at']
    
#     def __str__(self):
#         return self.name
    

class About(models.Model):
    title = models.CharField(max_length=200, help_text="Main heading for About section")
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Optional subheading")
    description = models.TextField(help_text="Detailed description about your company or service")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Upload an image for the About section")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

    def __str__(self):
        return self.title