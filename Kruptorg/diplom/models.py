from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=30, verbose_name='Номер заказа') #NOT null?
    date = models.DateTimeField(verbose_name='Дата отгрузки')
    status = models.CharField(max_length=30, verbose_name='Статус') #по дефолту "Принят"
    car_number = models.CharField(max_length=30, verbose_name='Номер машины')
    trailer_number = models.CharField(max_length=30, blank = True, verbose_name='Номер прицепа') #номер прицепа
    places = models.IntegerField(verbose_name='Количество мест всего')
    names = models.IntegerField(verbose_name='Кол-во наименований')
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date', )

    def __str__(self):
        return self.order_number


class OrderList(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Номер заказа')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    mass = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Масса НЕТТО')
    count = models.IntegerField(verbose_name='Количество')
    unit = models.CharField(max_length=20, verbose_name='Единица измерения')
    place = models.IntegerField(verbose_name='Количество мест')
    unit_place = models.IntegerField(verbose_name='Штука/место')

    class Meta:
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Составы заказов'

    def __str__(self):
        return self.order
