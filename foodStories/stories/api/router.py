from rest_framework.routers import DefaultRouter
from stories.api.views import StoryViewSet, UserViewSet, RecipeViewSet,\
                              CategoryViewSet, CommentViewSet, ContactViewSet,\
                              TagViewSet, CarViewSet

router = DefaultRouter()
router.register(r'story_list', StoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

router.register(r'cars', CarViewSet)

