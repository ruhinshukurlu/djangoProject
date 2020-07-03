from django.shortcuts import render,redirect
from stories.forms import ContactModelForm,StoryForm, AddNumbersForm, RecipeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic import TemplateView
from stories.models import Story, AddResult
from django.contrib import messages
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from stories.api.serializers import StorySerializer

from stories.tasks import add, story_count
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

class AddNumbersView(FormView):
    form_class = AddNumbersForm
    template_name = 'add-numbers.html'
    success_url = 'numbers/add'

    def form_valid(self, form):
        x = form.cleaned_data['x']
        y = form.cleaned_data['y']
        result = add.delay(x,y)
        AddResult.objects.create(result = result.get())
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return super().form_invalid(form)


class HomeView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class StoryView(CreateView):
    
    template_name = 'create_story.html'
    form_class = StoryForm


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(self.request.user)
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('stories:Home'))
        return render(request,self.template_name, {'form' : form})
    
    

class RecipeView(CreateView):
    template_name = 'create_story.html'
    form_class = RecipeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
        return render(request,self.template_name, {'form' : form})


class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.template_name, {'form' : form})



def recipes(request):
    return render(request, 'recipes.html')

def stories(request):
    return render(request, 'stories.html')

def single(request):
    return render(request, 'single.html')

def user_profile(request):
    return render(request, 'user-profile.html')

def email_subscribers(request):
    return render(request, 'email-subscribers.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')

def forget_password(request):
    return render(request, 'accounts/forget_password.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def reset_password(request):
    return render(request, 'accounts/reset_password.html')


@csrf_exempt
def story_list(request):
    """
    List all code story, or create a new story.
    """
    if request.method == 'GET':
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def story_detail(request, pk):
    """
    Retrieve, update or delete a story.
    """
    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StorySerializer(story)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StorySerializer(story, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        story.delete()
        return HttpResponse(status=204)
