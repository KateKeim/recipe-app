from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import RecipesSearchForm, CreateRecipeForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def about_view(request):
    return render(request, 'recipes/about.html')


class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


@login_required
def records(request):
    form = RecipesSearchForm(request.POST or None)
    recipe_df = None
    recipe_diff = None
    chart = None
    qs = None
    if request.method == 'POST':
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        if recipe_diff == '#2':
            recipe_diff = 'Medium'
        if recipe_diff == '#3':
            recipe_diff = 'Intermediate'
        if recipe_diff == '#4':
            recipe_diff = 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:  # if the data is found, convert the queryset values to pandas dataframe
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df)

            recipe_df = pd.DataFrame(qs.values(), columns=['id', 'name'])

            links = []

            for e, nam in enumerate(recipe_df['name']):
                nam = '<a href="/list/' + \
                    str(recipe_df['id'][e]) + '">' + str(nam) + '</a>'
                links.append(nam)

            recipe_df['name'] = links

            # convert the dataframe to HTML
            recipe_df = recipe_df.to_html(index=False, escape=False)

    # print(recipe_genre)
    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }

    return render(request, 'recipes/search.html', context)


# @login_required
def create_view(request):
    create_form = CreateRecipeForm(request.POST or None, request.FILES)
    name = None
    cooking_time = None
    ingredients = None
    description = None
    # pic = None

    if request.method == 'POST':

        try:
            recipe = Recipe.objects.create(
                name=request.POST.get('name'),
                cooking_time=request.POST.get('cooking_time'),
                ingredients=request.POST.get('ingredients'),
                description=request.POST.get('description'),
                # pic=request.POST.get('pic')
            )

            recipe.save()

        except:
            print('Error!!!')

    context = {
        'create_form': create_form,
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'description': description,
        # 'pic': pic
    }

    return render(request, 'recipes/create.html', context)
