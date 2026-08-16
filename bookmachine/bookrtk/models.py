import uuid
from django.db import models


class RtkPresent(models.Model):
    machine_model = models.CharField(max_length=100) # rtk base and rover or total station or rtk rover only
    # machine_brand = models.CharField(max_length=100) # gintec, chcnav or kolida
    # machine_name = models.CharField(max_length=100)  # 
    machine_description = models.CharField(max_length=100)
    machine_daily_rate = models.IntegerField()


class BookingDetails(models.Model):

    # booking_reference = 
    machine_booked = models.CharField(max_length=100)

    name_of_person_booking = models.CharField(max_length=50)
    phone_of_person_booking = models.CharField(max_length=13)
    email_of_person_booking = models.EmailField(max_length=100)
    # 
    # project = models.CharField(max_length=50) #toposurvey, subdivision, etc
    project_location = models.CharField(max_length=50) #ruiru, kiambu etc
    # number_of_days_to_book = models.IntegerField(default=1)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    # booking_date = models.DateField()
    # payment_method = models.CharField(max_length=20) #mpesa, bank transfer or cash
    booking_made_on = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=2000)


class Visitors(models.Model):
    session_id = models.CharField(max_length=255, blank=True)
    ip_addres_of_visitor = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    visiting_time = models.DateTimeField(auto_now_add=True)


# Create your models here.
