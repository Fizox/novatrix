from django.db import models


class ContactSubmission(models.Model):
    SERVICE_CHOICES = [
        ('new_website', 'New Website Design'),
        ('redesign', 'Website Redesign'),
        ('web_app', 'Web Application'),
        ('maintenance', 'Maintenance & Support'),
        ('ecommerce', 'E-Commerce Platform'),
        ('performance', 'Performance Optimization'),
        ('not_sure', 'Not Sure Yet'),
    ]

    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    current_website = models.URLField(blank=True, null=True)
    service_needed = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'

    def __str__(self):
        return f"{self.full_name} - {self.company_name} ({self.submitted_at.strftime('%Y-%m-%d')})"
