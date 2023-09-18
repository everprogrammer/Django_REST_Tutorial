from collections.abc import Iterable
from django.db import models
import phonenumbers
from phonenumbers.phonenumberutil import NumberFormatException
from django.core.exceptions import ValidationError

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=15)
    operating_airline = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80, null=True)
    email = models.EmailField(max_length=80)
    phone_number = models.CharField()

    def clean(self) -> None:
        try:
            parsed_number = phonenumbers.parse(self.phone_number, None)

            # Check if the number is valid
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError('Invalid phone number format')
            self.phone_number = phonenumbers.format_number(parsed_number, 
                                                           phonenumbers.PhoneNumberFormat.E164)
        except:
            raise ValidationError('Invalid phone number format')
        

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Reservation(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    


