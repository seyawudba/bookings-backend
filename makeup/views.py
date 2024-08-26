# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from makeup.models import Profile, Promotion
from makeup.serializers import ProfileSerializer, PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
