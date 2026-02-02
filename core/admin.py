from django.contrib import admin

from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'company_name', 'email', 'service_needed', 'submitted_at']
    list_filter = ['service_needed', 'submitted_at']
    search_fields = ['full_name', 'company_name', 'email', 'phone_number']
    readonly_fields = ['submitted_at']
    date_hierarchy = 'submitted_at'
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'company_name', 'email', 'phone_number')
        }),
        ('Project Details', {
            'fields': ('current_website', 'service_needed', 'project_description')
        }),
        ('Metadata', {
            'fields': ('submitted_at',)
        }),
    )

