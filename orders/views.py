from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderSerializer, OrderItemSerializer


class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderCreateSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(
            order__id=order_id,
            order__user=self.request.user
        ).select_related('product')


class OrderItemDetailView(generics.RetrieveAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(
            order__id=order_id,
            order__user=self.request.user,
        ).select_related('product')
