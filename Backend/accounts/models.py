from django.db import models
from django.contrib.auth.models import AbstractUser
from campus.models import Campus
# Create your models here.
# 관리자가 User 대체
class User(AbstractUser):
  name = models.CharField(max_length=20)
  belong = models.CharField(max_length=10)
  phone = models.CharField(max_length=13)
  authority_code = models.CharField(max_length=10)
  rfid_num = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

  class Manager(models.TextChoices):
    JUNIOR = 'JR', _('Junior')
    SENIOR = 'SR', _('Senior')
    MASTER = 'MR', _('Master')
  
  manager = models.CharField(max_length=2, choices=Manager.choices, default=Manager.JUNIOR)


  def __str__(self):
    return self.username