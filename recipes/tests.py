from django.test import TestCase
from .models import Recipe

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
