from django.contrib import admin
from .models import Brand, Category, Product, ProductLine


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 1
    can_delete = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    inlines = [ProductLineInline]


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    pass
