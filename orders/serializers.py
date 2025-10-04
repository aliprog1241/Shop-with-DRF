# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from catalog.models import Product

class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "price")

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "user", "created_at", "paid", "items")
        read_only_fields = ("user", "created_at", "items")

class OrderCreateSerializer(serializers.Serializer):
    items = OrderItemInputSerializer(many=True)

    def validate(self, attrs):
        # مثال ولیدیشن سطح بالا
        items = attrs["items"]
        if len(items) == 0:
            raise serializers.ValidationError("At least one item is required.")
        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        order = Order.objects.create(user=request.user)
        for it in validated_data["items"]:
            product = Product.objects.get(pk=it["product_id"], is_active=True)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=it["quantity"],
                price=product.price
            )
        return order
