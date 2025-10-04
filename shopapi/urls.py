
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/<str:version>/auth/", include("accounts.urls")),   # JWT, ثبت‌نام
    path("api/<str:version>/catalog/", include("catalog.urls")), # محصولات
    path("api/<str:version>/orders/", include("orders.urls")),   # سفارش‌ها
]
