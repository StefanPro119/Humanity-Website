from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Charity(models.Model):
    gooddoer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_doer')
    description = models.CharField(max_length=200)
    image = ResizedImageField(size=[500, 500], quality=100, null=True, blank=True, upload_to="images/")
    address = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gooddoer}"