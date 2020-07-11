from django.test import TestCase
from stories.models import Category

from django.contrib.auth import get_user_model
User = get_user_model()

class CategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'testing',
            email = 'test@gmail.com',
        )
        
        self.category = Category.objects.create(
            title = 'Category title'
        )

        