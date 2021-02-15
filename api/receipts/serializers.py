from rest_framework import serializers
from products.models import Product
from .models import Receipt
from django.contrib.auth.models import User

"""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =('id','description')
"""

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'description', 'created_at', 'updated_at', 'url', 'user', 'products')