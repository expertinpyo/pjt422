from datetime import datetime
from turtle import ondrag
from django.db import models
from campus.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.

# 기존 설계 계획
# 하루 단위로 레코드 생성
# 하루에 총 24개의 데이터

class Number(models.Model):
    num = models.CharField(max_length=4)

    class Meta:
        abstract = True

class Year(Number):    
    pass


class Month(Number):
    year = models.ForeignKey(Year, related_name='month', on_delete=models.CASCADE)


class Date(Number):
    hour_00 = models.IntegerField(default=0)
    hour_01 = models.IntegerField(default=0)
    hour_02 = models.IntegerField(default=0)
    hour_03 = models.IntegerField(default=0)
    hour_04 = models.IntegerField(default=0)
    hour_05 = models.IntegerField(default=0)
    hour_06 = models.IntegerField(default=0)
    hour_07 = models.IntegerField(default=0)
    hour_08 = models.IntegerField(default=0)
    hour_09 = models.IntegerField(default=0)
    hour_10 = models.IntegerField(default=0)
    hour_11 = models.IntegerField(default=0)
    hour_12 = models.IntegerField(default=0)
    hour_13 = models.IntegerField(default=0)
    hour_14 = models.IntegerField(default=0)
    hour_15 = models.IntegerField(default=0)
    hour_16 = models.IntegerField(default=0)
    hour_17 = models.IntegerField(default=0)
    hour_18 = models.IntegerField(default=0)
    hour_19 = models.IntegerField(default=0)
    hour_20 = models.IntegerField(default=0)
    hour_21 = models.IntegerField(default=0)
    hour_22 = models.IntegerField(default=0)
    hour_23 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        abstract = True


class BuildingDate(Date):
    # name = models.CharField(max_length=20, unique=True)
    building_month = models.ForeignKey(Month, related_name='building_date', on_delete=models.CASCADE)


class FloorDate(Date):
    # name = models.CharField(max_length=20)
    building_pk = models.IntegerField()
    floor_month = models.ForeignKey(Month, related_name='floor_date', on_delete=models.CASCADE)


class TrashbinDate(Date):
    
    
    class TypeOfTrash(models.TextChoices):
        GENERAL = 'GER', _('General')
        PLASTIC = 'PET', _('Plastic')
        CAN = 'CAN', _('Can')
        GLASS = 'GLA', _('Glass')
        PAPER = 'PPR', _('Paper')

    token = models.CharField(max_length=20)
    floor_pk = models.IntegerField()
    trash_type = models.CharField(
        max_length=3,
        choices=TypeOfTrash.choices,
        default=TypeOfTrash.GENERAL
    )
    trashbin_month = models.ForeignKey(Month, related_name='trashbin_date', on_delete=models.CASCADE)

