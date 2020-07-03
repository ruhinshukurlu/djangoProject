from django import forms
from django.forms import ModelForm
from stories.models import Contact,Subscribe,Story, Recipe

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

class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        fields = ("title",'description','category','storie_img',)

        widgets = {
            'title' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter title',
            }),
            'description' : forms.Textarea(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter description',
            }),
            'category' : forms.Select(attrs = {
                'class' : 'form-control',
            }),
        }

class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ("title",'description','category','recipe_img',)

        widgets = {
            'title' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter title',
            }),
            'description' : forms.Textarea(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter description',
            }),
            'category' : forms.Select(attrs = {
                'class' : 'form-control',
            }),
        }




class AddNumbersForm(forms.Form):
    x = forms.IntegerField(required=False, label = 'X')
    y = forms.IntegerField(required=False, label = 'Y')
        

