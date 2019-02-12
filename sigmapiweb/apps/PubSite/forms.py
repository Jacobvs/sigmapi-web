"""
Forms for Public Site (i.e. contact us).
"""
from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    """
    Form for submitting an email to the EC
    """
    sender = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    response_email = forms.EmailField()
