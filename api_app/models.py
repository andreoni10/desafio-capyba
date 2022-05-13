from django.db import models

class Films(models.Model):
    film_name = models.CharField(max_length=200)
    film_release = models.IntegerField()
    film_genre = models.CharField(max_length=200)
