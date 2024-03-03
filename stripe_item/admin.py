from django.contrib import admin
from .models import Item

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']
    list_filter = ['price', 'currency']
    search_fields = ['name', 'description']

