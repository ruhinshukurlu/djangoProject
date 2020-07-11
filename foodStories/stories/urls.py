from django.urls import path
from stories.views import HomeView,StoryCreateView,AboutView,ContactView, single,\
     AddNumbersView, RecipeView, NotifySubscribers, StoryListView, RecipeListView
from stories.api.urls import urlpatterns as api_urls

app_name = 'stories'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('about', AboutView.as_view(), name='About'),
    path('contact', ContactView.as_view(), name='contact'),
    path('create_story', StoryCreateView.as_view(), name='create_story'),
    path('story_list/', StoryListView.as_view(), name='Stories'),
    path('create_recipe', RecipeView.as_view(), name='create_recipe'),
    path('recipes', RecipeListView.as_view(), name='recipes'),
    path('single', single, name='single'),
    path('numbers/add', AddNumbersView.as_view(), name = 'add-numbers'),
    path("notify", NotifySubscribers.as_view(), name="notify-subscribers"),
] 