from django.urls import path, include
from .views import home
from .views import RecipesListView
from .views import RecipeDetailView
from .views import records
from .views import create_view

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipesListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', records, name='search'),
    path('create/', create_view, name='create'),
]
