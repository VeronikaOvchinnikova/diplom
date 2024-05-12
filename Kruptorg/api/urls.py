from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AddOrderView, AddOrderListView

v1_router = DefaultRouter()
v1_router.register('AddOrder', AddOrderView, basename='AddOrder')
v1_router.register('AddOrderList', AddOrderListView, basename='AddOrderList')

urlpatterns = [
    path('', include(v1_router.urls)),
]



