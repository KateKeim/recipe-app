from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
