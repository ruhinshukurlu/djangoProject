from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from stories.api.views import UserRegisterView

from stories.api.router import router

app_name = 'api'


urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('register', UserRegisterView.as_view()), 
]