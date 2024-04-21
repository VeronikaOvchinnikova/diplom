from django.contrib import admin
from .models import Order, OrderList


admin.site.empty_value_display = 'не задано'
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'date',
        'status',
        'car_number',
        'trailer_number',
        'places',
        'names'
    )
    list_editable = (
        'status',
    )
    search_fields = (
        'order_number',
    )
    list_filter = (
        'date',
        'status'
    )
class OrderInline(admin.TabularInline):
    model = Order

@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'name',
        'mass',
        'count',
        'unit',
        'place',
        'unit_place'
    )
    list_editable = (
        'mass',
    )
    search_fields = (
        'name',
        'order'
    )
    list_filter = (
        'name',
    )
class OrderListInline(admin.TabularInline):
    model = OrderList


