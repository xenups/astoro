from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
from version.models import AstorologyVersion
from version.serializers import AstrologySerializer


class AstorologyVersionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AstorologyVersion.objects.all()
    serializer_class = AstrologySerializer


class AstorologyVersionList(generics.ListCreateAPIView):
    queryset = AstorologyVersion.objects.all()
    serializer_class = AstrologySerializer
