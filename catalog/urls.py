
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet
from .views import (
    CategoryListCreateAPIView, ReviewListCreateAPIView, ReviewRetrieveUpdateAPIView,
    ProductListLimitOffsetAPIView, ProductListCursorAPIView,
)

router = DefaultRouter()
router.register("products-vs", ProductViewSet, basename="products-vs")

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("products/lo/", ProductListLimitOffsetAPIView.as_view()),
    path("products/cursor/", ProductListCursorAPIView.as_view()),
    path("products/<int:product_id>/reviews/", ReviewListCreateAPIView.as_view()),
    path("reviews/<int:pk>/", ReviewRetrieveUpdateAPIView.as_view()),
]
