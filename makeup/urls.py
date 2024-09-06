from django.urls import include, path
from rest_framework import routers

from makeup import views

router = routers.DefaultRouter()
router.register(r"promotions", views.PromotionViewSet, basename="promotion")
router.register(r"certificate", views.CertificateViewSet, basename="certificate")
router.register(r"portfolio", views.PortfolioViewSet, basename="porfolio")


urlpatterns = urlpatterns = [
    path("", include(router.urls)),
]
