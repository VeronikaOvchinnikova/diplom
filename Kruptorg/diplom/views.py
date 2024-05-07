from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order, OrderList
from api.serializers import OrderSerializer


class IndexListView(ListView, LoginRequiredMixin):
    paginate_by = 10
    model = Order
    template_name = 'index.html'

    @action(
        methods=['POST', 'PATCH'],
        detail=False,
        permission_classes=(IsAuthenticated, ),
        url_path='add_order',
        url_name='add_order'
    )
    def add_order(self, request):
        pass

    def get_queryset(self):
        return self.model.objects.get(
            'order_number',
            'date',
            'status',
            'car_number',
            'trailer_number',
            'places',
            'names').filter(status__in=[
            'Entered',
            'Accepted',
            'Assembly',
            'Awaiting shipment',
            'Is shipped',
            'Changed',
            'Has problem']).annotate(orders_count=Count('order_number')).order_by('-date')


def page_not_found(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def server_error(request):
    template = 'pages/500.html'
    return render(request, template, status=500)


def csrf_failure(request, reason=''):
    template = 'pages/403_csrf.html'
    return render(request, template, status=403)


def login(request):
    template = 'pages/login.html'
    form = AuthenticationForm()
    return render(request, template, {'form':form})


def login_request(request):
    return JsonResponse({'status':'OK'})




