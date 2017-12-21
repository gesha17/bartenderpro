from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cocktail(models.Model):
    name = models.CharField(max_length= 120)
    category = models.CharField(max_length=30)
    ingredients = models.CharField(max_length= 1300)
    recipe = models.CharField(max_length= 3000)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    difficulty = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    likes = models.CharField(max_length=6)
    dislikes = models.CharField(max_length=6)
    comment = models.CharField(max_length=3000)
    date = models.CharField(max_length=100)

class Post(models.Model):
    user = models.CharField(max_length=120)
    cocktail = models.CharField(max_length=120)
    comment = models.CharField(max_length=120)