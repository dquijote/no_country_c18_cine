from django.db import models

# Create your models here.

class Movies(models.Model):

    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    duration = models.IntegerField(unique=False)
    starring = models.CharField(unique=False, max_length=200)
    description = models.CharField(unique=False, max_length=500)
    genre = models.CharField(unique=False, max_length=20)
    
    def __repr__(self):
        return f"<Movies(id={self.movie_id}, name='{self.name}', duration={self.duration}, starring='{self.starring}', description='{self.starring}', genre='{self.genre}')>"
    