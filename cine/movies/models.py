from django.db import models

# Create your models here.

class Movies(models.Model):

    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    duration = models.IntegerField(unique=False)
    starring = models.CharField(unique=False, max_length=200)
    description = models.CharField(unique=False, max_length=500)
    genre = models.CharField(unique=False, max_length=20)
    
    def __str__(self):
        return self.movie_id