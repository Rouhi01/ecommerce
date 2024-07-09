from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(instance=self.queryset, many=True)
        return Response(data=serializer.data)

