from django.contrib import admin
from .models import Brand, Category, Product, ProductLine


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    pass
