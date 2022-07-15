from django.db import models
from django.contrib.auth.models import AbstractUser
from buildings.models import Trashbin

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    #belong = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username



class SchoolPeople(models.Model):
    name = models.CharField(max_length=100)
    trashbins = models.ManyToManyField(Trashbin, related_name='trash_people')
    #belong = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name