from venv import create
from auth_user.models import Customer

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = [ 'username', 'first_name', 'last_name', 'last_name2',
                  'email', 'picture', 'gender',]
   