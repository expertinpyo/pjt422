from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Campus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='building')

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=100)
    map_path = models.TextField()
    width = models.FloatField()
    height = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floor')

    def __str__(self):
        return self.name


class Trashbin(models.Model):
    class TypeOfTrash(models.TextChoices):
        GENERAL = 'GER', _('General')
        PLASTIC = 'PET', _('Plastic')
        CAN = 'CAN', _('Can')
        GLASS = 'GLA', _('Glass')
        PAPER = 'PPR', _('Paper')
    
    class CurrentState(models.TextChoices):
        SAFE = 'SAF', _('Safe')
        CAUTION = 'CAU', ('Caution')
        WARNING = 'WAR', ('Warning')
        

    token = models.CharField(max_length=200)
    # 쓰레기 종류 코드 => 공통코드
    trash_type = models.CharField(
        max_length=3,
        choices=TypeOfTrash.choices,
        default=TypeOfTrash.GENERAL
    )
    current_amount = models.FloatField()
    total_amount = models.FloatField()
    # status
    status = models.CharField(
        max_length=3,
        choices=CurrentState.choices,
        default=CurrentState.SAFE
    )
    location_x = models.FloatField()
    location_y = models.FloatField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='trashbin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discard_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='discard_trashbin')  #비우는거


class Student(models.Model):
    student_num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    belong = models.CharField(max_length=100)
    rfid_num = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.name



