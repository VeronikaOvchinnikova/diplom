from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexListView, login

app_name='diplom'

urlpatterns = [
    path('', IndexListView.as_view(), name='main_page',),
    path('login/', login, name='login')
]