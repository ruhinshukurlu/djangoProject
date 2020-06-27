from rest_framework.routers import DefaultRouter
from stories.api.views import StoryViewSet, UserViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'users', UserViewSet)


