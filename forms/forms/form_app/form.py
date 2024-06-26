
from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea)
    
    
    def send_email(self):
        print(f"sending email from {self.cleaned_data['email']} with message {self.cleaned_data['message']}")
