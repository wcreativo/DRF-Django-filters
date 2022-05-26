from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RestaurantView, SchoolStudentAPIView

urlpatterns = [
    path('', SchoolStudentAPIView.as_view(), name='school'),
    path('restaurants/', RestaurantView.as_view(), name='resturants')
]
