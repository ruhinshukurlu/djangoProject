from django.urls import path
from stories.views import HomeView,StoryView,AboutView,ContactView ,recipes,stories,single,user_profile,email_subscribers,change_password,forget_password,login,register,reset_password

app_name = 'stories'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('about', AboutView.as_view(), name='About'),
    path('contact', ContactView.as_view(), name='contact'),
    path('create_story', StoryView.as_view(), name='create_story'),
    path('recipes', recipes, name='recipes'),
    path('stories', stories, name='stories'),
    path('single', single, name='single'),
    path('user_profile', user_profile, name='user_profile'),
    path('email_subscribers', email_subscribers, name='email_subscribers'),
    path('change_password', change_password, name='change_password'),
    path('forget_password', forget_password, name='forget_password'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('reset_password', reset_password, name='reset_password'),
]