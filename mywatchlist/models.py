from django.db import models

class MovieList(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()

# Create your models here.
