from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import MenuItemFilter
from .models import MenuItem, Restaurant, School
from .serializers import ResturantSerializer, SchoolSerializer


class SchoolStudentAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    queryset              = School.objects.all()
    serializer_class      = SchoolSerializer
    filter_backends       = (DjangoFilterBackend,)
    filter_fields         = ('is_government','students__is_adult')

    def list(self, request, *args, **kwargs):
            resp = super().list(request, *args, **kwargs)
            from django.db import connection
            print(connection.queries) # or set a breakpoint here
            return resp

class RestaurantView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResturantSerializer
    
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('menu_items__name',)

    def get_queryset(self):
        queryset = Restaurant.objects.prefetch_related(
            Prefetch('menu_items', queryset=MenuItem.objects.filter(is_removed=False), to_attr='filtered_menu_items')
        )
        return queryset
