from django.db import models
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class Distributor(models.Model):
    name = models.CharField(max_length=120) #max_length is required
    address = models.TextField(blank=False, null=False)
    phone = models.CharField(max_length=20) #max_length is required
    web_link = models.CharField(max_length=150) #max_length is required

