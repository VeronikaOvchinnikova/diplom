from django.contrib import admin
from .models import Order, OrderList, OrderStatusChangeHistory, Comments
from rest_framework.authtoken.models import Token



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


@admin.register(OrderStatusChangeHistory)
class OrderStatusChangeHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'status',
        'status_changed_time',
        'status_changed_by'
    )
    list_editable = (
        'status',
    )
    search_fields = (
        'order',
    )
    list_filter = (
        'status_changed_time',
        'status_changed_by',
        'status'
    )


class OrderStatusChangeHistoryInline(admin.TabularInline):
    model = OrderStatusChangeHistory


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author',
        'created_at',
        'order_number'
    )

    search_fields = (
        'author',
    )
    list_filter = (
        'order_number',
        'author'
    )


class CommentsInline(admin.TabularInline):
    model = Comments


# def create_token(modeladmin, request, queryset):
#     for user in queryset:
#         Token.objects.get_or_create(user=user)
#
#
# create_token.short_description = 'Создать токены для выбранных пользователь'
#
#
# class UserAdmin (admin.ModelAdmin):
#     actions = [create_token]
#
# class TokenAdmin (admin.ModelAdmin):
#     list_display = ('key', 'user', 'created')
#     fields = ('user', )
#
#
# # admin.site.register(UserToken, TokenAdmin)