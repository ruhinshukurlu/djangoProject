from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def creat_story(request):
    return render(request, 'create_story.html')

def contact(request):
    return render(request, 'contact.html')

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
