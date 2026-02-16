from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.CartView.as_view(), name='cart'),
    path('items/<int:pk>/', views.CartItemDetailView.as_view(), name='items_detail'),
]