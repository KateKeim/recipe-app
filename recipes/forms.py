# import django forms
from django import forms

# specify choices as a tuple
CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFIC__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)

# define class-based Form imported from Django forms


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)


class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=255)
    cooking_time = forms.IntegerField(help_text='in minutes')
    ingredients = forms.CharField(max_length=500)
    description = forms.CharField(max_length=500)
    # pic = forms.ImageField(upload_to='recipes', default='food-photo.jpg')
