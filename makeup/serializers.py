from django.contrib.auth import get_user_model
from rest_framework import serializers

from makeup.models import Certificate, MakeUpArtist, Portfolio, Promotion

user = get_user_model()


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["id", "title", "description", "start", "end"]


class CertificateSerializer(serializers.ModelSerializer):
    artist = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate
        fields = ["title", "artist", "cert_image"]

    def create(self, validated_data):
        artist_id = self.context["artist_id"]

        return Certificate.objects.create(artist=artist_id, **validated_data)


class PortfolioSerializer(serializers.ModelSerializer):
    artist_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Portfolio
        fields = ["title", "artist_id", "portfolio_image"]

    def create(self, validated_data):
        artist_id = self.context["artist_id"]

        return Portfolio.objects.create(artist=artist_id, **validated_data)


class MakeUpArtistSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MakeUpArtist
        fields = ["id", "user_id", "bio_experience", "social_media_link"]

    def create(self, validated_data):
        user_id = self.context["user_id"]

        return MakeUpArtist.objects.create(user_id=user_id, **validated_data)
