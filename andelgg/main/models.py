from django.db import models


class DB(models.Model):
    name = models.CharField(max_length=16)
    text = models.CharField(max_length=64)
