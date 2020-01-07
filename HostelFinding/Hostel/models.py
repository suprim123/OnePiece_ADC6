from django.db import models

# Create your models here.
class Hostel(models.Model):
    Name = models.CharField(max_length=25)
    Location = models.CharField(max_length=50)
    Category = models.CharField(max_length=10)
    Picture = models.ImageField()


    def __str__(self):
     return self.Name

