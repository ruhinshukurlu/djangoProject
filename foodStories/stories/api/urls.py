from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from stories.api.views import   story_detail, story_list,\
                                 api_root

from stories.api.router import router

# urlpatterns = [
#     path('api/story_list', StoryGenericList.as_view()),
#     path('api/story_list/<int:pk>', StoryGenericDetail.as_view()),
#     path('api/users/', UserList.as_view()),
#     path('api/users/<int:pk>/', UserDetail.as_view()),
#     path('api', api_root),
#     path('api/stories/<int:pk>/highlight/', StoryHighlight.as_view()),
# ]

app_name = 'api'

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('story_list/',
#         StoryGenericList.as_view(),
#         name='story-list'),
#     path('story_list/<int:pk>/',
#         StoryGenericDetail.as_view(),
#         name='story-detail'),
#     path('story_list/<int:pk>/highlight/',
#         StoryHighlight.as_view(),
#         name='story-highlight'),
#     path('users/',
#         UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         UserDetail.as_view(),
#         name='user-detail')
# ])

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]

urlpatterns = [
    path('', include(router.urls))
]
