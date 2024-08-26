# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from makeup.models import Promotion
from makeup.serializers import PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
