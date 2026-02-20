from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<int:order_id>/items/', views.OrderItemListView.as_view(), name='order_item_list'),
    path('<int:order_id>/items/<int:pk>/', views.OrderItemDetailView.as_view(), name= 'order_item_detail'),
]