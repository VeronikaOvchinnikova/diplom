from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexListView, login_view, logout_view, ArchiveListView, change_status, send_comment

app_name = 'diplom'

urlpatterns = [
    path('', IndexListView.as_view(), name='main_page',),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('archive/', ArchiveListView.as_view(), name='archive'),
    path('change_status/', change_status, name='change_status'),
    path('send_comment/', send_comment, name='send_comment')
]