from rest_framework import serializers
from stories.models import Story

from django.contrib.auth import get_user_model
User = get_user_model()

class StorySerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='api:story-highlight', format='html')

    class Meta:
        model = Story
        fields = ['url', 'id', 'highlight', 'author','title', 'description']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    stories = serializers.HyperlinkedRelatedField(many=True, view_name='api:user-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url','id', 'username', 'stories']