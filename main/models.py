from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1000)

class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Rating(models.Model):
    meal = models.ForeignKey(Meal)
    user = models.ForeignKey(User)
    value = models.IntegerField()