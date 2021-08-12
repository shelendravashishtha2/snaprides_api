from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = "__all__"
        depth=2
        