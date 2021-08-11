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