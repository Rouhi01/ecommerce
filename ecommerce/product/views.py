from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(data=serializer.data)

