# Generated by Django 5.1 on 2024-08-24 13:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegresionLineal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajoRemoto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'RegresionLineal',
                'verbose_name_plural': 'RegresionesLineales',
                'db_table': 'RegresionLineal',
                'ordering': ['myuser', '-myuser'],
            },
        ),
        migrations.CreateModel(
            name='RegresionLogistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajoRemoto', models.CharField(max_length=35)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'RegresionLogistica',
                'verbose_name_plural': 'RegresionesLogisticas',
                'db_table': 'RegresionLogistica',
                'ordering': ['myuser', '-myuser'],
            },
        ),
    ]
