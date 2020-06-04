from django.urls import path
from stories import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='contact'),
    path('create_story', views.create_story, name='create_story'),
    path('recipes', views.recipes, name='recipes'),
    path('stories', views.stories, name='stories'),
    path('single', views.single, name='single'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('email_subscribers', views.email_subscribers, name='email_subscribers'),
    path('change_password', views.change_password, name='change_password'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('reset_password', views.reset_password, name='reset_password'),
]