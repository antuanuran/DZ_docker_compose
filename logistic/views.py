from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        # 1. Сериалайзер: ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    lookup_field = 'title'                      # Поиск по описанию, а не по id


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer          # 3. Сериалайзер: StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']


