from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout

from .models import Order, OrderList
from api.serializers import OrderSerializer


class IndexListView(ListView, LoginRequiredMixin):
    paginate_by = 10
    pk_url_kwarg = 'order_pk'
    model = Order
    template_name = 'pages/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        # return self.model.objects.select_related(
        #     'order_number',
        #     'date',
        #     'status',
        #     'car_number',
        #     'trailer_number',
        #     'places',
        #     'names').
        #     filter(status__in=[

        return self.model.objects.filter(status__in=[
            'Entered',
            'Accepted',
            'Assembly',
            'Awaiting shipment',
            'Is shipped',
            'Changed',
            'Has problem']).prefetch_related('items').all()


class ArchiveListView(ListView, LoginRequiredMixin):
    paginate_by = 10
    pk_url_kwarg = 'order_pk'
    model = Order
    template_name = 'pages/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.filter(status__in=[
            'Canceled',
            'Shipped']).prefetch_related('items').all()


def page_not_found(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def server_error(request):
    template = 'pages/500.html'
    return render(request, template, status=500)


def csrf_failure(request, reason=''):
    template = 'pages/403_csrf.html'
    return render(request, template, status=403)


def login_view(request):
    template = 'pages/login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('diplom:main_page')
    else:
        form = AuthenticationForm()
    return render(request, template, {'form':form})


# def login(request):
#     template = 'pages/login.html'
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('diplom:main_page')
#     else:
#         form = AuthenticationForm()
#     return render(request, template, {'form':form})



def logout_view(request):
    logout(request)
    return redirect('diplom:login')




