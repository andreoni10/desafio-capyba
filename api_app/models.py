from django.db import models

class Films(models.Model):
    film_name = models.CharField(max_length=100)
    film_release = models.IntegerField()
    film_genre = models.CharField(max_length=50)

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_image_url = models.CharField(max_length=100)