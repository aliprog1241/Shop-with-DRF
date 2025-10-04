
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    #jwt
    path("api/<str:version>/auth/", include("accounts.urls")),
    # for products
    path("api/<str:version>/catalog/", include("catalog.urls")),
    #for orders
    path("api/<str:version>/orders/", include("orders.urls")),
]
