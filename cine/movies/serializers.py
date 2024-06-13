from rest_framework import serializers
from .models import Movies,Showtimes

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class ShowtimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtimes
        fields = '__all__'
        extra_kwargs = {'price':{'required':False}}
       
    def validate(self, data):
        date = data.get('date')
        if date:
            weekday = date.weekday()
            if weekday in [0, 1, 2, 3]:  # Lunes a Jueves
                data['price'] = 10
            elif weekday in [4,5]:  # Viernes y Sábado
                data['price'] = 15
            else:  # Domingo
                data['price'] = 12
        return data