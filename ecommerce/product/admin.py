from django.contrib import admin
from .models import Brand, Category, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
