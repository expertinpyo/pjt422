from email.policy import default
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

# 기본 틀이 되는 클래스, only 상속받기 위한 용도
class DefaultInfo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Building(DefaultInfo):
    description = models.TextField()

    def __str__(self):
        return self.name


class Floor(DefaultInfo):
    map_path = models.TextField()
    width = models.FloatField()
    height = models.FloatField()
    trashbin_size = models.FloatField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floor')
    order = models.IntegerField()   # 층 순서
    
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
        
    token = models.CharField(max_length=200, null=False)
    # 쓰레기 종류 코드 => 공통코드
    trash_type = models.CharField(
        max_length=3,
        choices=TypeOfTrash.choices,
        default=TypeOfTrash.GENERAL
    )
    amount = models.FloatField(default=0)
    # status
    status = models.CharField(
        max_length=3,
        choices=CurrentState.choices,
        default=CurrentState.SAFE
    )
    location_x = models.FloatField()
    location_y = models.FloatField()
    group = models.CharField(max_length=5)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='trashbin')
    is_connected = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discard_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='discard_trashbin', through='CleanRecord')  # 쓰레기통을 비운 관리잔

    def __str__(self):
        return self.token


class Student(DefaultInfo):
    student_num = models.CharField(max_length=100)
    belong = models.CharField(max_length=100)
    rfid_num = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class CleanRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trashbin = models.ForeignKey(Trashbin, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
