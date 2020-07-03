from rest_framework import serializers
from stories.models import Story, Recipe, Comment, Category, Contact, Tag, Car

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'bio', 'profile_img']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        def create(self, validated_data):
            user = User.objects.create(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                email = validated_data['last_name']
            )
            password = validated_data['password']
            user.set_password(password)
            user.save()
            return user


class StorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Story
        fields = ['id', 'author','title', 'category' ,'description']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'author','title', 'category' ,'description']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_time']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'category_img']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fileds = ['id', 'name', 'email', 'subject', 'message']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class CarModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ['id', 'title','description','price','image']
