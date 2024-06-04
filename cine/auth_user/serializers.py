from venv import create
from auth_user.models import Customer

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = [ 'username', 'first_name', 'last_name', 'last_name2',
                  'email', 'picture', 'gender',]

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
   