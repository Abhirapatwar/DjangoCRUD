from django.db import models

class Entries(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
