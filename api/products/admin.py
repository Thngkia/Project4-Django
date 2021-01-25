# Register your models here.
from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):  # add this
    list_display = ('id', 'barcode', 'description', 'manufacturer', 'price', 'cost', 'inventory')  # add this


admin.site.register(Product, ProductAdmin)  # add this
