# Generated by Django 5.0.4 on 2024-05-16 04:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0006_comments_orderstatuschangehistory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatuschangehistory',
            options={'verbose_name': 'История заказа', 'verbose_name_plural': 'История заказов'},
        ),
        migrations.AlterField(
            model_name='orderstatuschangehistory',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderstatuschangehistory',
            name='status_changed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кто сменил статус'),
        ),
        migrations.AlterField(
            model_name='orderstatuschangehistory',
            name='status_changed_time',
            field=models.DateField(auto_now_add=True, verbose_name='Время смены статуса'),
        ),
    ]
