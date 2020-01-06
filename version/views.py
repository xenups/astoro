from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from version import models
from version.models import AstorologyVersion
from version.serializers import AstrologySerializer




class AstorologyVersionList(generics.ListAPIView):
    queryset = AstorologyVersion.objects.all()
    serializer_class = AstrologySerializer

    def get_object(self):
        version = get_object_or_404(models.AstorologyVersion)
        return version
