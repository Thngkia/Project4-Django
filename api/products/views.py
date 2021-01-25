# Create your views here.
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()