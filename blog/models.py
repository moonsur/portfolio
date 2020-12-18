from django.db import models
from django.utils.timezone import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField(default='')
    image = models.ImageField(upload_to='media/')
