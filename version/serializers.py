from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from .models import AstorologyVersion


class AstrologySerializer(serializers.ModelSerializer, ):
    class Meta:
        model = AstorologyVersion
        fields = ['min_version', 'current_version']
