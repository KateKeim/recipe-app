from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
        return str(self.name)
