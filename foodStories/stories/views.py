from django.shortcuts import render,redirect
from stories.forms import ContactModelForm,StoryForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.


class HomeView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class StoryView(View):
    template_name = 'create_story.html'
    form_class = StoryForm

    def get(self,request,*args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'StoryForm' : form})

    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'StoryForm' : form})



class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.template_name, {'form' : form})



def recipes(request):
    return render(request, 'recipes.html')

def stories(request):
    return render(request, 'stories.html')

def single(request):
    return render(request, 'single.html')

def user_profile(request):
    return render(request, 'user-profile.html')

def email_subscribers(request):
    return render(request, 'email-subscribers.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')

def forget_password(request):
    return render(request, 'accounts/forget_password.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def reset_password(request):
    return render(request, 'accounts/reset_password.html')
