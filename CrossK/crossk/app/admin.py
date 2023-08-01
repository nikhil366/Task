from django.contrib import admin
from app.models import (Category, Item, ItemPrice)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemPrice)
class ItemPriceAdmin(admin.ModelAdmin):
    pass