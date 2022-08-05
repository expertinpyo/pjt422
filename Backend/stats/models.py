from django.db import models
from campus.models import Trashbin

# Create your models here.

# 기존 설계 계획
# 하루 단위로 레코드 생성
# 하루에 총 24개의 데이터
class DateStats(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

class CampusStats(models.Model):
    pass

class BuildingStats(models.Model):
    pass

class FloorStats(models.Model):
    pass

class TrashbinStats(models.Model):
    pass
