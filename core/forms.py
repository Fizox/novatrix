from django import forms

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = [
            'full_name',
            'company_name',
            'email',
            'phone_number',
            'current_website',
            'service_needed',
            'project_description'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'John Smith',
                'required': True
            }),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Your Company Inc.',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'john@company.com',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+1 (555) 123-4567'
            }),
            'current_website': forms.URLInput(attrs={
                'placeholder': 'https://yourwebsite.com'
            }),
            'service_needed': forms.Select(attrs={
                'required': True
            }),
            'project_description': forms.Textarea(attrs={
                'placeholder': 'Describe your needs, goals, and timeline...',
                'required': True
            }),
        }
        labels = {
            'full_name': 'Full Name *',
            'company_name': 'Company Name *',
            'email': 'Email Address *',
            'phone_number': 'Phone Number',
            'current_website': 'Current Website (if any)',
            'service_needed': 'What do you need? *',
            'project_description': 'Tell us about your project *',
        }
