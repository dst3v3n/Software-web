# Generated by Django 5.1 on 2024-08-25 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('powerbi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nucleo_familiar', models.CharField(choices=[('Persona soltera', 'Persona soltera'), ('Pareja con hijos dependientes', 'Pareja con hijos dependientes'), ('Familia monoparental con hijos dependientes', 'Familia monoparental con hijos dependientes'), ('Hogar multifamiliar', 'Hogar multifamiliar'), ('Otro hogar unifamiliar', 'Otro hogar unifamiliar'), ('Hogar grupal', 'Hogar grupal'), ('', 'selecciona tu nucleo familiar'), ('Pareja sin hijos dependientes', 'Pareja sin hijos dependientes')], default='', max_length=50)),
                ('cambios_trabajo', models.CharField(choices=[('Algo probable', 'Algo probable'), ('Ni poco probable ni probable', 'Ni poco probable ni probable'), ('', 'selecciona tu respuesta'), ('Muy probable', 'Muy probable'), ('Algo improbable', 'Algo improbable'), ('Muy improbable', 'Muy improbable')], default='Muy probable', max_length=40)),
                ('tiempoDesplazamiento', models.DecimalField(decimal_places=1, max_digits=10)),
                ('horasDomestica', models.DecimalField(decimal_places=1, max_digits=10)),
                ('horasPersonal', models.DecimalField(decimal_places=1, max_digits=10)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'db_table': 'perfiles',
                'ordering': ['myuser', '-myuser'],
            },
        ),
        migrations.CreateModel(
            name='powerbi_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powerbi.categorias')),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'powerbi_user',
                'verbose_name_plural': 'powerbi_user',
                'db_table': 'powerbi_user',
                'ordering': ['myuser', '-myuser'],
            },
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoDedicado', models.DecimalField(decimal_places=1, max_digits=10)),
                ('position', models.CharField(choices=[('Agricultura, silvicultura y pesca', 'Agricultura, silvicultura y pesca'), ('', 'Selecciona su sector'), ('Finanzas y seguros', 'Finanzas y seguros'), ('Alojamiento y alimentos', 'Alojamiento y alimentos'), ('Electricidad, gas, agua y desechos', 'Electricidad, gas, agua y desechos'), ('Salud', 'Salud'), ('Alquiler, arrendamiento y bienes raíces', 'Alquiler, arrendamiento y bienes raíces'), ('Medios de información y telecomunicaciones', 'Medios de información y telecomunicaciones'), ('Minería', 'Minería'), ('Construcción', 'Construcción'), ('Comercio minorista', 'Comercio minorista'), ('Profesionales, científicos y técnicos', 'Profesionales, científicos y técnicos'), ('Transporte, postal y almacenamiento', 'Transporte, postal y almacenamiento'), ('Manufactura', 'Manufactura'), ('Atención de la salud y asistencia social', 'Atención de la salud y asistencia social'), ('Administración pública y seguridad', 'Administración pública y seguridad'), ('Educación y formación', 'Educación y formación'), ('Comercio mayorista', 'Comercio mayorista'), ('Otros servicios', 'Otros servicios'), ('Artes y recreación', 'Artes y recreación'), ('Administración y apoyo', 'Administración y apoyo')], default='', max_length=105, null=True)),
                ('sector', models.CharField(choices=[('Operadores de maquinaria y conductores - Operadores de plantas móviles', 'Operadores de maquinaria y conductores - Operadores de plantas móviles'), ('Profesionales - Profesionales en negocios, recursos humanos y mercadeo', 'Profesionales - Profesionales en negocios, recursos humanos y mercadeo'), ('Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas', 'Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas'), ('Obreros - Obreros de construcción y minería', 'Obreros - Obreros de construcción y minería'), ('Técnicos y trabajadores calificados - Trabajadores calificados en alimentos', 'Técnicos y trabajadores calificados - Trabajadores calificados en alimentos'), ('Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones', 'Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones'), ('Profesionales - Profesionales de la salud', 'Profesionales - Profesionales de la salud'), ('Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes', 'Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes'), ('Profesionales - Profesionales de las artes y los medios', 'Profesionales - Profesionales de las artes y los medios'), ('Gerentes - Agricultores y gerentes de granjas', 'Gerentes - Agricultores y gerentes de granjas'), ('Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos', 'Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos'), ('Gerentes - Gerentes especializados', 'Gerentes - Gerentes especializados'), ('Obreros - Trabajadores de procesos en fábricas', 'Obreros - Trabajadores de procesos en fábricas'), ('Profesionales - Profesionales de TIC', 'Profesionales - Profesionales de TIC'), ('Obreros - Trabajadores de granjas, silvicultura y jardines', 'Obreros - Trabajadores de granjas, silvicultura y jardines'), ('Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte', 'Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte'), ('Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería', 'Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería'), ('Trabajadores de oficina y administrativos - Asistentes personales y secretarias', 'Trabajadores de oficina y administrativos - Asistentes personales y secretarias'), ('Operadores de maquinaria y conductores - Almacenistas', 'Operadores de maquinaria y conductores - Almacenistas'), ('Obreros - Limpiadores y trabajadores de lavandería', 'Obreros - Limpiadores y trabajadores de lavandería'), ('Profesionales - Profesionales en derecho, social y bienestar', 'Profesionales - Profesionales en derecho, social y bienestar'), ('Obreros - Asistentes de preparación de alimentos', 'Obreros - Asistentes de preparación de alimentos'), ('Profesionales - Profesionales en educación', 'Profesionales - Profesionales en educación'), ('', 'Selecciona su cargo'), ('Trabajadores de ventas - Asistentes de ventas y vendedores', 'Trabajadores de ventas - Asistentes de ventas y vendedores'), ('Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril', 'Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril'), ('Trabajadores de ventas - Apoyo a las ventas', 'Trabajadores de ventas - Apoyo a las ventas'), ('Gerentes - Gerentes de hostelería, retail y servicios', 'Gerentes - Gerentes de hostelería, retail y servicios'), ('Trabajadores de ventas - Representantes y agentes de ventas', 'Trabajadores de ventas - Representantes y agentes de ventas'), ('Técnicos y trabajadores calificados - Trabajadores calificados en construcción', 'Técnicos y trabajadores calificados - Trabajadores calificados en construcción'), ('Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados', 'Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados'), ('Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias', 'Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias'), ('Gerentes - Directores ejecutivos, gerentes generales y legisladores', 'Gerentes - Directores ejecutivos, gerentes generales y legisladores'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería', 'Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería'), ('Trabajadores de oficina y administrativos - Apoyo clerical y de oficina', 'Trabajadores de oficina y administrativos - Apoyo clerical y de oficina'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar', 'Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar'), ('Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas', 'Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas'), ('Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia', 'Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección', 'Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección'), ('Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura', 'Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura'), ('Trabajadores de oficina y administrativos - Trabajadores clericales generales', 'Trabajadores de oficina y administrativos - Trabajadores clericales generales'), ('Trabajadores de oficina y administrativos - Oficinistas numéricos', 'Trabajadores de oficina y administrativos - Oficinistas numéricos'), ('Obreros - Otros obreros', 'Obreros - Otros obreros')], default='', max_length=105, null=True)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'trabajo',
                'verbose_name_plural': 'trabajos',
                'db_table': 'trabajos',
                'ordering': ['myuser', '-myuser'],
            },
        ),
    ]
