# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from makeup.models import Certificate, Portfolio, Promotion
from makeup.serializers import (
    CertificateSerializer,
    PortfolioSerializer,
    PromotionSerializer,
)


class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()


# a particular make up artist
# request query params artist__id==23
class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        # user_id = self.request.user.id
        artist_id = self.request.query_params.get("artist__id")
        if artist_id is not None:
            return Certificate.objects.filter(artist_id=artist_id)
        return Certificate.objects.all()


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        # user_id = self.request.user.id
        artist_id = self.request.query_params.get("artist__id")
        if artist_id is not None:
            return Portfolio.objects.filter(artist_id=artist_id)
        return Portfolio.objects.all()
