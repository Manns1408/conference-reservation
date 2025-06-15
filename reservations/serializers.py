from rest_framework import serializers
from .models import Rooms, TheReservation
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheReservation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
