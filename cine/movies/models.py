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
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    
class Showtimes(models.Model):

    st_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    price = models.IntegerField(unique=False)
    date = models.DateField(unique=False, max_length=10)
    time = models.TimeField(unique=False, max_length=6)
    
    def __repr__(self):
        return f"{self.movie.name},{self.time},{self.date},{self.price}"
    
    class Meta:
        verbose_name = "Showtime"
        verbose_name_plural = "Showtimes"