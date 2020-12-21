from django.db import models
from django.utils.timezone import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField(default='')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

    def pub_date_short(self):
        return self.pub_date.strftime("%b %d %Y")
