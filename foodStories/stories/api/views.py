from rest_framework import status
from stories.models import Story
from stories.api.serializers import StorySerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from stories.api.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from rest_framework import viewsets
from rest_framework.decorators import action

from django.contrib.auth import get_user_model
User = get_user_model()





@api_view(['GET', 'POST'])
def story_list(request):
    """
    List all stories, or create a new story.
    """
    if request.method == 'GET':
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def story_detail(request, pk):
    """
    Retrieve, update or delete a story.
    """
    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StorySerializer(story)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryList(APIView):
    """
    List all stories, or create a new story.
    """
    def get(self, request, format=None):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StoryDetail(APIView):
    """
    Retrieve, update or delete a story instance.
    """
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class StoryGenericList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer

#     def perform_create(self, serializer):
#         serializer.save(AUTHOR=self.request.user)


# class StoryGenericDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly]
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer

# class StoryHighlight(generics.GenericAPIView):
#     queryset = Story.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         story = self.get_object()
#         return Response(story.highlighted)


class StoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(story.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'stories': reverse('story-list', request=request, format=format)
    })


