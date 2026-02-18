from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'children']

    def get_children(self, obj):
        serializer = CategorySerializer(obj.children.all(), many=True)
        return serializer.data



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
