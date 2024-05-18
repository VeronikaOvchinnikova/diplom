from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

ROLE_CHOICES = (
    ('Storekeeper', 'Кладовщик'),
    ('Manager', 'Менеджер')
)

STATUS_CHOICES = (
    ('Поступил', 'Поступил'),
    ('Принят', 'Принят'),
    ('В сборке', 'В сборке'),
    ('Ожидает отгрузки', 'Ожидает отгрузки'),
    ('Отгружается', 'Отгружается'),
    ('Отгружен', 'Отгружен'),
    ('Отменен', 'Отменен'),
    ('Изменен', 'Изменен'),
    ('Возникла проблема', 'Возникла проблема')
)


User = get_user_model()

class Order(models.Model):
    """Модель заказа."""
    order_number = models.CharField(max_length=30,
                                    verbose_name='Номер заказа',
                                    unique=True)
    date = models.DateField(verbose_name='Дата отгрузки', blank=True)
    status = models.CharField(max_length=30,
                              verbose_name='Статус', default='Поступил', choices=STATUS_CHOICES)
    car_number = models.CharField(max_length=30,
                                  verbose_name='Номер машины', blank=True)
    trailer_number = models.CharField(max_length=30,
                                      blank=True,
                                      verbose_name='Номер прицепа')
    places = models.IntegerField(verbose_name='Количество мест всего')
    names = models.IntegerField(verbose_name='Количество наименований')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date', )

    def __str__(self):
        return self.order_number


class OrderList(models.Model):
    """Модель состава заказа."""
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              verbose_name='Номер заказа')
    name = models.CharField(max_length=200,
                            verbose_name='Наименование')
    mass = models.DecimalField(max_digits=20,
                               decimal_places=3,
                               verbose_name='Масса НЕТТО')
    count = models.IntegerField(verbose_name='Количество')
    unit = models.CharField(max_length=20,
                            verbose_name='Единица измерения')
    place = models.IntegerField(verbose_name='Количество мест')
    unit_place = models.IntegerField(verbose_name='Штука/место')

    class Meta:
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Составы заказов'

    def __str__(self):
        return self.name


class Comments (models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateField(verbose_name='Дата комментария', auto_now_add=True)
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа', related_name='comments')

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f'Комментарий пользователя: {self.author}'


class OrderStatusChangeHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    status = models.CharField(max_length=50, verbose_name='Статус')
    status_changed_time = models.DateField(auto_now_add=True, verbose_name='Время смены статуса')
    status_changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Кто сменил статус')

    class Meta:
        verbose_name = 'История заказа'
        verbose_name_plural = 'История заказов'

    def __str__(self):
        return f'{self.status} сменен {self.status_changed_by}'

# class UserToken(Token):
#
#     class Meta:
#         proxy = True
#         ordering = ('username', )