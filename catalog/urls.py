# catalog/urls.py
from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductUpdateAPIView,
    ProductListLimitOffsetAPIView, ProductListCursorAPIView,
    ReviewListCreateAPIView, ReviewRetrieveUpdateAPIView,
)

urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("products/", ProductListAPIView.as_view()),
    path("products/lo/", ProductListLimitOffsetAPIView.as_view()),   # LimitOffset
    path("products/cursor/", ProductListCursorAPIView.as_view()),    # Cursor
    path("products/create/", ProductCreateAPIView.as_view()),
    path("products/<slug:slug>/", ProductRetrieveAPIView.as_view()),
    path("products/<slug:slug>/update/", ProductUpdateAPIView.as_view()),
    path("products/<int:product_id>/reviews/", ReviewListCreateAPIView.as_view()),
    path("reviews/<int:pk>/", ReviewRetrieveUpdateAPIView.as_view()),
]
