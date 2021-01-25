from rest_framework import serializers

from .models import Receipt
from django.contrib.auth.models import User

class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Receipt
        fields = ('id', 'description', 'created_at', 'updated_at', 'url', 'user', 'products')


