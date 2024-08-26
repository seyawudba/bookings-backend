from django.urls import include, path
from rest_framework import routers

from makeup import views

router = routers.DefaultRouter()
router.register(r"promotions", views.PromotionViewSet, basename="promotion")
router.register(r"profile", views.ProfileViewSet, basename="profile")

urlpatterns = urlpatterns = [
    path("", include(router.urls)),
]
