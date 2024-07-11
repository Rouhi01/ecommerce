import factory
from ecommerce.product.models import Category, Brand, Product

"""FOR EVERY MODEL WE CREATE IT"""


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brond"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_product"
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    """BECAUSE OF RELATION WITH OTHER TABLE"""