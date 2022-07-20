from django.db import models
from django.conf import settings
from accounts.models import SchoolPeople

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Floor(models.Model):
    floor = models.CharField(max_length=10)
    floor_building = models.ForeignKey(Building, related_name='building_floor', on_delete=models.CASCADE)

class Trashbin(models.Model):
    types = models.CharField(max_length=10)
    current_amount = models.FloatField()
    total_amount = models.FloatField()
    last_discarded = models.DateTimeField(auto_now=True)
    location_x = models.FloatField()
    location_y = models.FloatField()
    trashbin_floor = models.ForeignKey(Floor, related_name='floor_trashbin', on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 관리자와 쓰레기통은 1:N관계


class Trash(models.Model):
    trashbin = models.ForeignKey(Trashbin, on_delete=models.CASCADE)
    discard_date = models.DateTimeField(add_now_add=True)
    people = models.ForeignKey(SchoolPeople, on_delete=models.CASCADE)