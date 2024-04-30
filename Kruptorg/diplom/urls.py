from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexListView



urlpatterns = [
    path('', IndexListView.as_view(), name='main_page',),
]