from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexListView, login_view, logout_view

app_name = 'diplom'

urlpatterns = [
    path('<int:order_pk>', IndexListView.as_view(), name='main_page',),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]