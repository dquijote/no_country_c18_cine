from django.db import models
from auth_user.models import Customer

# Create your models here.
class Cart(models.Model):
    amount = models.IntegerField("Costo")
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.amount

    def __unicode__(self):
        return 

class Ticket(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    seat = models.OneToOneField("Seat", on_delete=models.CASCADE, default=None)
    refence = models.CharField("Referencia", max_length=250)

    def __str__(self):
        return self.refence

    def __unicode__(self):
        return     

class Seat(models.Model):
    screen = models.ForeignKey("Screen", on_delete=models.CASCADE, default=None)
    seat_number = models.IntegerField("Numero de asiento")
    occupied = models.BooleanField("Ocupado")

    def __str__(self):
        return self.seat_number

    def __unicode__(self):
        return       

class Screen(models.Model):
    screen_number = models.IntegerField("Numero")

    def __str__(self):
        return self.screen_number

    def __unicode__(self):
        return     