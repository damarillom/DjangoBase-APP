from django.urls import path
from django.urls.conf import include
from .viewsets import ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]