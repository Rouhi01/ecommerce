from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(instance=self.queryset, many=True)
        return Response(data=serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewSet for viewing all brands
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        serializer = BrandSerializer(instance=self.queryset, many=True)
        return Response(data=serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple viewSet for viewing all products
    """
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(instance=self.queryset, many=True)
        return Response(data=serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r'category/(?P<category>\w+)/all',
        url_name="all")
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to return product by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)



