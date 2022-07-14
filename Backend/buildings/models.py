from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Location(models.Model):
    floor = models.CharField(max_length=10)
    x = models.FloatField()
    y = models.FloatField()
    floor_building = models.ForeignKey(Building, related_name='building_floor')

class Trashbin(models.Model):
    types = models.CharField(max_length=10)
    current_amount = models.FloatField()
    total_amount = models.FloatField()
    last_discarded = models.DateTimeField(auto_now=True)
    trashbin_location = models.ForeignKey(Location, related_name='location_trashbin')
    
