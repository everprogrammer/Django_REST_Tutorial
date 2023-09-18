from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(self, flight_number):
        if (re.match("^[a-zA-Z0-9]*$", flight_number)==None):
            raise serializers.ValidationError('Invalid Flight Number!')
        return flight_number


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

