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

    def uploaddata_name_blank(self):
        if self.Name == "":
            return True
        else:
            return False

   
    def uploadata_fields_blank(self):
        return(self.Name != True)

    def TestWork(self):
        return (work_HO((self.Location) >= 3) and work_HO((self.Location) <= 50))
       
    def Price_fields_blank(self):
        return (self.Price!= False)
 
    def workdes_field_blank(self):
        return ((self.Description != True ) and (self.Description) <= 50)

     

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



    def uploaddata_name_blank(self):
        if self.Name == "":
            return True
        else:
            return False

   
    def uploadata_fields_blank(self):
        return(self.Name != True)

    def TestWork(self):
        return (work_HO((self.Location) >= 3) and work_HO((self.Location) <= 50))
       
    def Price_fields_blank(self):
        return (self.Price!= False)
 
    def workdes_field_blank(self):
        return ((self.Description != True ) and (self.Description) <= 50)


