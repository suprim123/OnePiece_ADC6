from django.db import models

# Create your models here.
class Hostel(models.Model):
    Name = models.CharField(max_length=25)
    Location = models.CharField(max_length=50)
    Price = models.IntegerField
    Picture = models.ImageField()
    Description = models.TextField()


    def __str__(self):
     return self.Name

