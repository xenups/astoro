from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .utility import DateConvert
from feedback.models import FeedBack
from feedback.permissions import FeedBackPermission, IsAuthenticatedNotPost
from feedback.serializers import FeedBackSerializer


class FeedBackList(generics.ListCreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (IsAuthenticatedNotPost,)

    def perform_create(self, serializer):
        if self.request.data is not None:
            date_time_str = self.request.data['birthday']
            serializer.save(birthday=DateConvert.jalali_to_georgian(jalali_date=date_time_str))
