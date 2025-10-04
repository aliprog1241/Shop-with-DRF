# catalog/serializers.py
from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = ("id", "title", "slug", "price", "stock", "is_active",
                  "created_at", "category", "category_id")

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("عنوان باید حداقل ۳ کاراکتر باشد.")
        return value

    def validate(self, attrs):
        price = attrs.get("price", getattr(self.instance, "price", None))
        stock = attrs.get("stock", getattr(self.instance, "stock", None))
        if price is not None and price <= 0:
            raise serializers.ValidationError({"price": "قیمت باید بزرگ‌تر از صفر باشد."})
        if stock is not None and stock < 0:
            raise serializers.ValidationError({"stock": "موجودی نمی‌تواند منفی باشد."})
        return attrs

