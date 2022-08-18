from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Trashbin)
admin.site.register(CleanRecord)