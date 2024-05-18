from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .permission import IsStorekeeper, IsManager
from django.contrib import messages

from .models import Order, OrderList, OrderStatusChangeHistory
from api.serializers import OrderSerializer
from .forms import CommentForm


class IndexListView(ListView):
    paginate_by = 10
    pk_url_kwarg = 'order_pk'
    model = Order
    template_name = 'pages/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        order = self.request.GET.get('order')
        queryset = self.model.objects.filter(status__in=[
            'Поступил',
            'Принят',
            'В сборке',
            'Ожидает отгрузки',
            'Отгружается',
            'Изменен',
            'Возникла проблема']).prefetch_related('items').all()
        if order == 'date':
            return queryset.order_by('date')
        return queryset.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['today_orders_count'] = self.model.objects.filter(date=today).count()
        context['changes_order_count'] = self.model.objects.filter(status='Изменен').count()
        context['isstorekeeper'] = self.request.user.groups.filter(name='Кладовщик').exists()
        return context

def send_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.order = Order.objects.get(order_number=request.POST.get('order_number'))
        comment.author = request.user
        comment.save()
        print('Все ок')
        return redirect('diplom:main_page')


class ArchiveListView(ListView, LoginRequiredMixin):
    paginate_by = 10
    pk_url_kwarg = 'order_pk'
    model = Order
    template_name = 'pages/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.filter(status__in=[
            'Отменен',
            'Отгружен']).prefetch_related('items').all()


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


def change_status(request):
    if request.method == 'POST':
        order_number = request.POST.get('order_number')
        status = request.POST.get('status')
        order = Order.objects.get(order_number=order_number)
        old_status = order.status
        order.status = status
        order.save()
        OrderStatusChangeHistory.objects.create(order=order, status=f'{old_status} -> {status}', status_changed_by=request.user)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def logout_view(request):
    logout(request)
    return redirect('diplom:login')




