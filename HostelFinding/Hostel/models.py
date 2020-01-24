from django.db import models

# Create your models here.
class Hostel(models.Model):
    Name = models.CharField(max_length=25)
    Price = models.CharField(max_length=7)
    Description = models.TextField()
    addresses = models.ManyToManyField('Location')


    def __str__(self):
     return f"{self.Name} has record {self.Price}"

     

class Location(models.Model):
    Name=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
      

class HostelDetails(models.Model):
	Description = models.CharField(max_length=20)
	Hostel = models.OneToOneField(Hostel, on_delete = models.CASCADE)
	Price = models.IntegerField(default=0)
	

class user(models.Model):
    Name = models.CharField(max_length = 50)
    Location = models.CharField(max_length=30)
    Hostels = models.ForeignKey(Hostel, on_delete=models.CASCADE)