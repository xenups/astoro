import datetime
from .utility import DateConvert
import jdatetime
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from .models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = FeedBack
        fields = ['name', 'feedback', 'birthday', 'firebase_token', 'star', 'is_premium_user']

    def validate_date_of_birth(self, value):
        if value.birthday < 1360:
            raise serializers.ValidationError("wrong birhtday")
        return value

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        date_time_str = ret['birthday']
        if date_time_str is not None:
            ret['birthday'] = DateConvert.georgian_to_jalali(ret['birthday'])
        return ret
