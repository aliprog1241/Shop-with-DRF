# catalog/viewsets.py
from rest_framework import viewsets, permissions, decorators, response, status
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes_by_action = {
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
        "create": [permissions.IsAdminUser],
        "update": [permissions.IsAdminUser],
        "partial_update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
        "toggle_active": [permissions.IsAdminUser],
    }

    def get_permissions(self):
        return [perm() for perm in self.permission_classes_by_action.get(self.action, [permissions.IsAuthenticated])]

    @decorators.action(detail=True, methods=["post"])
    def toggle_active(self, request, slug=None):
        product = self.get_object()
        product.is_active = not product.is_active
        product.save()
        return response.Response({"is_active": product.is_active}, status=status.HTTP_200_OK)
