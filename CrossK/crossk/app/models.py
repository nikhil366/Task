from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Category(BaseModel):
    name = models.CharField(max_length=100)


class FitingType(models.TextChoices):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XL = "XL"


class Item(BaseModel):
    brand_name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    fitting_type = models.CharField(max_length=50, choices=FitingType.choices)
    is_imported = models.BooleanField(default=False)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')


class ItemPrice(BaseModel):
    select_item = models.ForeignKey(
        Item, null=True, blank=True, on_delete=models.CASCADE, related_name='prices')
    price = models.FloatField(null=True, blank=True)
