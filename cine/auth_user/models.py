from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

genderOption = [
         ('Femenino', 'Femenino'),
         ('Masculino', 'Masculino'),

    ]


class Customer(AbstractUser):  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
          
    def custom_upload_to(instance, filename):
        try:
            ext = instance.picture.name[-4:]
            filename = str(instance.username) + "_" + str(instance.first_name) + str(ext)
            instance.picture.name = instance.first_name
        except Customer.DoesNotExist:
            pass
        return 'img/customer/' + str(filename)
  
    # personal_id = models.IntegerField("Identificador", unique=True)
    email = models.EmailField(max_length=150, unique=True)
    last_name2 = models.CharField("Segundo Apellido ", max_length=255, null=True)
    picture = models.ImageField("Foto", blank=True, default=None, upload_to=custom_upload_to)
    gender = models.CharField("Genero", choices=genderOption, max_length=150)
    # birthday = models.DateField("Fecha de nacimiento")
    

    def __str__(self):
        return self.first_name

    def __unicode__(self):
        return 
