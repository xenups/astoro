from django.db import models


# Create your models here.
class AstorologyVersion(models.Model):
    min_version = models.CharField(max_length=255, blank=False)
    current_version = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.current_version
