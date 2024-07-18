from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .managers import ActiveQueryset
from django.core.exceptions import ValidationError

from .custom_fields import OrderField


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = TreeForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_lines')
    is_active = models.BooleanField(default=False)
    order = OrderField(blank=True, unique_for_field="product")

    objects = ActiveQueryset.as_manager()

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        product_lines = ProductLine.objects.filter(product=self.product)
        for product_line in product_lines:
            if self.id != product_line.id and self.order == product_line.order:
                raise ValidationError("Duplicate value.")

    def __str__(self):
        return str(self.order)




