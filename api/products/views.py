# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['barcode', 'inventory', 'description', 'manufacturer']
