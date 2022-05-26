import django_filters

from .models import MenuItem


class MenuItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = MenuItem
        fields = ['name']
