# Generated by Django 5.1 on 2024-08-25 07:26

from django.db import migrations

def insert_initial_categories(apps, schema_editor):
    Categoria = apps.get_model('powerbi', 'categorias')

    # Crea instancias de categorias con datos iniciales
    Categoria.objects.create(name='horaDesplazamiento')
    Categoria.objects.create(name='horaHogar')
    Categoria.objects.create(name='horaFamilia')
    Categoria.objects.create(name='horasTrabajadas')
    Categoria.objects.create(name='prediccion')

class Migration(migrations.Migration):

    dependencies = [
        ('powerbi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_initial_categories),
    ]
