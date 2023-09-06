from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField(help_text='in minutes')
    ingredients = models.TextField()
    description = models.TextField(default='description')
    pic = models.ImageField(upload_to='recipes', default='food-photo.jpg')

    def calculate_difficulty(self):
        difficulty = None
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 7:
            difficulty = 'Hard'
        return difficulty

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)
