from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexListView, login, login_request

app_name='diplom'

urlpatterns = [
    path('', IndexListView.as_view(), name='main_page',),
    path('login/', login, name='login'),
    path('login_request/', login_request, name='login_request')
]