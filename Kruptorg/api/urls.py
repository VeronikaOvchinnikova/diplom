from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AddOrderView, AddOrderListView

v1_router = DefaultRouter()
v1_router.register('AddOrder', AddOrderView, basename='AddOrder')
v1_router.register('AddOrderList', AddOrderListView, basename='AddOrderList')
# v1_router.register('token/create', TokenCreationView, basename='TokenCreation')

urlpatterns = [
    path('', include(v1_router.urls))
]



