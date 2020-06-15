from django import forms
from django.forms import ModelForm
from stories.models import Contact,Subscribe

class ContactModelForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name","email","subject","message",)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Name',
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Email',
                }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Subject',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Message',
                'cols': 30, 
                'rows': 7,
                }),
        }

