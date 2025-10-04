# orders/urls.py
from django.urls import path
from .views import OrderListAPIView, OrderRetrieveAPIView, OrderCreateAPIView

urlpatterns = [
    path("", OrderListAPIView.as_view()),
    path("<int:pk>/", OrderRetrieveAPIView.as_view()),
    path("create/", OrderCreateAPIView.as_view()),
]
