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

# LimitOffsetPagination نمونه
class ProductLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

# CursorPagination نمونه
class ProductCursorPagination(pagination.CursorPagination):
    page_size = 10
    ordering = "-created_at"

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("title")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # فقط ادمین بسازد
    throttle_scope = "products"

