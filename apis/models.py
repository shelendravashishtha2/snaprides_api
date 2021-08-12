from django.db import models

# Create your models here.
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.fields import CharField, EmailField, ImageField

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
   


class Users(models.Model):
    first_name = models.CharField(max_length = 20,null = True, blank = True)
    last_name = models.CharField(max_length = 20,null = True, blank = True)
    email = models.EmailField()
    phone = models.IntegerField(unique=True)
    phone_varified = models.BooleanField(default=False)
    kyc_varified = models.BooleanField(default=False)
    user_image_url = models.ImageField(upload_to = 'static/Document', null = True, blank = True)
    aadhar_card_url = models.ImageField(upload_to = 'static/Document', null = True, blank = True)

class Address(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    landmark = models.CharField(max_length=120,blank=True, null=True)
    city_name = models.CharField(max_length=30)
    offer_code = models.CharField(max_length=30, blank=True, null=True)
    offer_discount = models.IntegerField(blank=True, null=True)
    station_start_timing = models.DateTimeField(auto_now_add=True)
    station_end_timing = models.DateTimeField(auto_now_add=True)

class Bikes(models.Model):
    bike_photo = models.ImageField(upload_to="static/Bikes",null=True, blank=True)
    company_name = models.CharField(max_length=30)
    bike_name = models.CharField(max_length=30)
    curr_available = models.IntegerField(default=0, blank=True, null=True)
    free_kms = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField()
    discount_on_price = models.IntegerField(null=True, blank=True)
    bikes_availability = models.ManyToManyField(Address)