from django.db import models
from django.contrib.auth.models import AbstractUser
from campus.models import Campus
from django.utils.translation import gettext_lazy as _
# Create your models here.
# User = 관리자

class User(AbstractUser):
    class Position(models.TextChoices):
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        MASTER = 'MR', _('Master')
    
    name = models.CharField(max_length=20,)
    belong = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    rfid_num = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, related_name="manager")
    # ENUM for manager's position
    position = models.CharField(max_length=2, choices=Position.choices, default=Position.JUNIOR)


    def __str__(self):
        return self.username