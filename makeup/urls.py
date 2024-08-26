from django.urls import include, path
from rest_framework import routers

from makeup import views

promotion = routers.DefaultRouter()
promotion.register(r"promotions", views.PromotionViewSet, basename="promotion")

urlpatterns = urlpatterns = [
    path("", include(promotion.urls)),
]
