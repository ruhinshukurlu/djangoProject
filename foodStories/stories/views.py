from django.shortcuts import render,redirect
from stories.forms import ContactModelForm,StoryForm, AddNumbersForm, RecipeForm, SubscribeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic import TemplateView, ListView, DetailView
from stories.models import Story, AddResult, Recipe, Category, Subscribe
from django.contrib import messages
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from stories.api.serializers import StorySerializer

from stories.tasks import add, story_count, nootify_subscriber
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(TemplateView):
   
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myStories"] = Story.objects.filter(author = self.request.user)[:3]
        context["recent_recipes"] = Recipe.objects.all()[:4]  
        print(context)      
        return context

class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class StoryCreateView(CreateView):
    
    template_name = 'create_story.html'
    form_class = StoryForm


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(self.request.user)
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
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
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('stories:Stories'))
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
            return HttpResponseRedirect(reverse_lazy('stories:Home'))
        return render(request,self.template_name, {'form' : form})


class StoryListView(ListView):
    model = Story
    template_name='stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        
        return context

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_recipes"] = Recipe.objects.all()[:3]
        return context

class StoryDetailView(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_recipes"] = Recipe.objects.all()[:3]
        return context

class SubscribeView(FormView):
    form_class = SubscribeForm
    template_name = 'subscribe.html'
    success_url = reverse_lazy('stories:Home')

    def form_valid(self, form):
        print('valid')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('invalid')
        messages.warning(self.request, 'Something went wrong!')
        return super().form_invalid(form)




class NotifySubscribers(View):
    template_name = 'notify.html'

    def get(self, request, *args, **kwargs):
        nootify_subscriber.delay()
        return render(request, self.template_name)

class AddNumbersView(FormView):
    form_class = AddNumbersForm
    template_name = 'add-numbers.html'
    success_url = '/numbers/add'

    def form_valid(self, form):
        x = form.cleaned_data['x']
        y = form.cleaned_data['y']
        result = add.delay(x,y)
        AddResult.objects.create(result = result.get())
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return super().form_invalid(form)
