# from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from makeup.models import Certificate, MakeUpArtist, Portfolio, Promotion
from makeup.serializers import (
    CertificateSerializer,
    MakeUpArtistSerializer,
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

    def get_serializer_context(self):
        user_id = self.request.user.id
        artist = MakeUpArtist.objects.get(user_id=user_id)
        return {"artist_id": artist}

    def get_queryset(self):
        # user_id = self.request.user.id
        artist_id = self.request.query_params.get("artist__id")
        if artist_id is not None:
            return Certificate.objects.filter(artist_id=artist_id)
        return Certificate.objects.all()


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer

    def get_serializer_context(self):
        user_id = self.request.user.id
        artist = MakeUpArtist.objects.get(user_id=user_id)
        return {"artist_id": artist}

    def get_queryset(self):
        # user_id = self.request.user.id
        artist_id = self.request.query_params.get("artist__id")
        if artist_id is not None:
            return Portfolio.objects.filter(artist_id=artist_id)
        return Portfolio.objects.all()


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = MakeUpArtistSerializer
    queryset = MakeUpArtist.objects.all()

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def get_serializer_context(self):
        user_id = self.request.user.id
        return {"user_id": user_id}

    @action(detail=False, methods=["GET", "PUT"])
    def me(self, request):
        artist, _ = MakeUpArtist.objects.get_or_create(user_id=self.request.user.id)
        if request.method == "GET":
            serializer = MakeUpArtistSerializer(artist)
            return Response(serializer.data)
        if request.method == "PUT":
            serializer = MakeUpArtistSerializer(artist, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
