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

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "products"
    pagination_class = SmallPageNumberPagination  # استفاده از Pagination سفارشی
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "slug", "category__title"]
    ordering_fields = ["price", "created_at"]

class ProductListLimitOffsetAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ProductLimitOffsetPagination

class ProductListCursorAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ProductCursorPagination

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]  # فقط ادمین
    throttle_scope = "products"

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = "slug"

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAdminUser]

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_scope = "reviews"

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        return Review.objects.filter(product_id=product_id)

    def perform_create(self, serializer):
        serializer.save()
