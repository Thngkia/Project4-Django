from django.contrib import admin

from .models import Receipt


class ReceiptAdmin(admin.ModelAdmin):  # add this
    list_display = ('id', 'description', 'created_at', 'updated_at', 'user')  # add this


admin.site.register(Receipt, ReceiptAdmin)  # add this

# Register your models here.
