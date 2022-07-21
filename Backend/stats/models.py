from django.db import models
from campus.models import Trashbin

# Create your models here.

# 기존 설계 계획
# 하루 단위로 레코드 생성
# 하루에 총 24개의 데
class Stats(models.Model):
  date = models.DateTimeField()
  time = models.CharField(max_length=15)
  empty_num = models.IntegerField()
  use_num = models.IntegerField()
  amount = models.FloatField()
  trashbin = models.ForeignKey(Trashbin, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.date