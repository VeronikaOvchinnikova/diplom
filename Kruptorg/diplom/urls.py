from django.urls import path
from . import views


app_name = 'diplom'
urlpatterns = [
    path('', views.IndexListView.as_view(), name = 'main_page'),
    path('<slug:category>/', views.index2)
]