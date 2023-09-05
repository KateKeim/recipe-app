from django.db import models

# Create your models here.


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField(help_text='in minutes')
    ingredients = models.TextField()

    def __str__(self):
        return self.name
