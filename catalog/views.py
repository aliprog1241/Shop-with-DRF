# catalog/views.py
from rest_framework import generics, permissions, pagination, filters
from rest_framework.throttling import ScopedRateThrottle
from .models import Product, Review, Category
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer

# Pagination اختصاصی (برای نمایش در یکی از ویوها)
class SmallPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = "page"
    max_page_size = 50

