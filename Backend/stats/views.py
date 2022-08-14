# class형 view를 만들기 위해 View import
from django.views.generic import View

from rest_framework.response import Response

from .models import *

# Create your views here.
class TotalView(View):

    def get(self, request):
        pass