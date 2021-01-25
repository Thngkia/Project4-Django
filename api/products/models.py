from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(null=True, max_length=255)
    manufacturer = models.CharField(null=True, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    barcode = models.CharField(null=True, max_length=12)

    def __str__(self):
        return '%d: %s' % (self.id, self.description)
