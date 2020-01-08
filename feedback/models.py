from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="نام")
    birthday = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    feedback = models.CharField(max_length=250, blank=True, verbose_name='نظر')
    firebase_token = models.CharField(max_length=250, blank=False)
    star = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)],
                               verbose_name='امتیاز')
    is_premium_user = models.BooleanField(default=False)
