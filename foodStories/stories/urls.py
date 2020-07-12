from django.urls import path
from stories.views import HomeView,StoryCreateView,AboutView,ContactView,\
     AddNumbersView, RecipeView, NotifySubscribers, StoryListView, RecipeListView,\
     SubscribeView, RecipeDetailView, StoryDetailView
from stories.api.urls import urlpatterns as api_urls

app_name = 'stories'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('about', AboutView.as_view(), name='About'),
    path('contact', ContactView.as_view(), name='contact'),
    path('create_story', StoryCreateView.as_view(), name='create_story'),
    path('story_list/', StoryListView.as_view(), name='Stories'),
    path('stories/<int:pk>', StoryDetailView.as_view(), name = 'story-detail'),
    path('create_recipe', RecipeView.as_view(), name='create_recipe'),
    path('recipes', RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name = 'recipe-detail'),
    path('subscribe', SubscribeView.as_view(), name = 'subscribe'), 
    path('numbers/add', AddNumbersView.as_view(), name = 'add-numbers'),
    path("notify", NotifySubscribers.as_view(), name="notify-subscribers"),
] 