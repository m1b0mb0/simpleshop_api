import django_filters
from .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_category')

    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt', 'range'],
        }
    
    def filter_category(self, queryset, name, value):
        try:
            category = Category.objects.get(slug=value)
        except Category.DoesNotExist:
            return queryset.none()

        categories = [category, *category.get_descendants()]

        return queryset.filter(category__in=categories)

