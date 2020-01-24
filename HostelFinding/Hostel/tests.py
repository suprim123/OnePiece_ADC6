
from django.test import TestCase, Client
from .models import Hostel
from django.urls import reverse, resolve



    # Create your tests here.
class ModelTestCase(TestCase):
   def setUp(self):
            hostel = Hostel.objects.create(Name="ram")
            location = Hostel.objects.create(Location="japan")
            price = Hostel.objects.create(Price= '900')

    def test_name(self):
        hostel = Hostel.objects.get(Name = "ram")
        self.assertEqual(hostel.Name, "naemi")

            
    def test_location(self):
        location = Hostel.objects.get(Location = "japan")
        self.assertEqual(location.Location, "dsajk")


    def test_price(self):
        price = Hostel.objects.get(Price = '900')
        self.assertEqual(price.Price, '808')

    def test_description(self):
        description = Hostel.objects.get(Description = 'lalallalalallalallalala')
        self.assertEqual(description.Description, 'lalallalalallalallalala')     
        
