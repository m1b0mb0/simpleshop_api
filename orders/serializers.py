from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'address', 
            'postal_code',
            'city',
            'total_cost',
            'paid',
            'created',
            'items' 
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'address',
            'postal_code',
            'city'
        ]
    
    def create(self, validated_data):
        user = self.context['request'].user
        cart = user.cart

        total_sum = cart.total_cost
        order = Order.objects.create(user=user, total_cost=total_sum, **validated_data)

        if not cart.items.exists():
            raise serializers.ValidationError("Cart is empty")

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.cost,
                quantity=item.quantity
            )
        
        cart.items.all().delete()

        return order
