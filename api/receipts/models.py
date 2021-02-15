from django.contrib.auth.models import User
from django.db import models


class Receipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    products = models.CharField(null=False, max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.id
