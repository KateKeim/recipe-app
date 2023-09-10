from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm
from .forms import CreateRecipeForm

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time=5,
                              ingredients='tea-leaves, water, sugar')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'in minutes')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_calculate_difficulty_easy(self):
        recipe = Recipe(name='Easy Recipe', cooking_time=5,
                        ingredients='apple, banana')
        difficulty = recipe.calculate_difficulty()
        self.assertEqual(difficulty, 'Easy')

    def test_calculate_difficulty_medium(self):
        recipe = Recipe(name='Medium Recipe', cooking_time=8,
                        ingredients='apple, banana, orange, pear, grape, wine, beer, whiskey')
        difficulty = recipe.calculate_difficulty()
        self.assertEqual(difficulty, 'Medium')

    def test_calculate_difficulty_hard(self):
        recipe = Recipe(name='Hard Recipe', cooking_time=30,
                        ingredients='apple, banana, orange, pear, grape, wine, beer, whiskey')
        difficulty = recipe.calculate_difficulty()
        self.assertEqual(difficulty, 'Hard')

    def test_get_absolute_url(self):
        recipe = Recipe(name='Test Recipe', cooking_time=15,
                        ingredients='apple, banana')
        url = recipe.get_absolute_url()
        self.assertEqual(url, '/list/None')

# ================================= CHART ====================================


class RecipesSearchFormTest(TestCase):

    def test_form_renders_recipe_diff_input(self):
        form = RecipesSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipesSearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())

# ================================= Create Recipe ====================================


class CreateRecipeFormTestCase(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'Spaghetti Carbonara',
            'cooking_time': 30,
            'ingredients': 'Pasta, Eggs, Bacon, Parmesan Cheese',
            'description': 'A classic Italian pasta dish with creamy sauce.'
        }
        form = CreateRecipeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form_data = {}
        form = CreateRecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])
        self.assertEqual(form.errors['cooking_time'], [
                         'This field is required.'])
        self.assertEqual(form.errors['ingredients'], [
                         'This field is required.'])
        self.assertEqual(form.errors['description'], [
                         'This field is required.'])

    def test_invalid_cooking_time(self):
        form_data = {
            'name': 'Pizza',
            'cooking_time': 'Invalid',
            'ingredients': 'Dough, Tomato Sauce, Cheese',
            'description': 'A classic Italian dish.'
        }
        form = CreateRecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['cooking_time'], [
                         'Enter a whole number.'])

    def test_name_length_exceeds_max_length(self):
        form_data = {
            'name': 'P' * 256,  # Exceeds max length of 255
            'cooking_time': 40,
            'ingredients': 'Cheese, Tomato, Basil',
            'description': 'A simple Italian dish.'
        }
        form = CreateRecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [
                         'Ensure this value has at most 255 characters (it has 256).'])
