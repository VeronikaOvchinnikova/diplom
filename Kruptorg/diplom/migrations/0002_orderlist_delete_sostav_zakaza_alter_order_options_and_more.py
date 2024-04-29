# Generated by Django 5.0.4 on 2024-04-29 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('mass', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Масса НЕТТО')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('unit', models.CharField(max_length=20, verbose_name='Единица измерения')),
                ('place', models.IntegerField(verbose_name='Количество мест')),
                ('unit_place', models.IntegerField(verbose_name='Штука/место')),
            ],
            options={
                'verbose_name': 'Состав заказа',
                'verbose_name_plural': 'Составы заказов',
            },
        ),
        migrations.DeleteModel(
            name='Sostav_zakaza',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='pricep_number',
        ),
        migrations.AddField(
            model_name='order',
            name='trailer_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер прицепа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='car_number',
            field=models.CharField(max_length=30, verbose_name='Номер машины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='Дата отгрузки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='names',
            field=models.IntegerField(verbose_name='Кол-во наименований'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=30, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='places',
            field=models.IntegerField(verbose_name='Количество мест всего'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=30, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='diplom.order', verbose_name='Номер заказа'),
        ),
    ]