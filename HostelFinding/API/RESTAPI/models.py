from django.db import models

class Host(models.Model):
    hostelName=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
