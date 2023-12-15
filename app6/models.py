from django.db import models

class Url(models.Model):
    long = models.URLField()
    short = models.CharField(max_length = 70)
    count = models.IntegerField(default = 0)