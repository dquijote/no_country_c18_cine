from django.contrib import admin
from cart.models import Cart, Seat, Screen, Ticket

# Register your models here.
admin.site.register(Cart)
admin.site.register(Seat)
admin.site.register(Screen)
admin.site.register(Ticket)