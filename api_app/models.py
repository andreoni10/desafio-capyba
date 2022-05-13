from django.db import models

class Films(models.Model):
    film_name = models.CharField(max_length=100)
    film_release = models.IntegerField()
    film_genre = models.CharField(max_length=50)