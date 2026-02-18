from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
