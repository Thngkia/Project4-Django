from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Receipt
from .serializers import ReceiptSerializer


class ReceiptView(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user']
