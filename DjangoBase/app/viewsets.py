from .models import Product
from .serialializers import ProductSerializer
from rest_framework import viewsets

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer