# Generated by Django 5.1 on 2024-08-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Dirección electronico')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('position', models.CharField(choices=[('Manufactura', 'Manufactura'), ('Alquiler, arrendamiento y bienes raíces', 'Alquiler, arrendamiento y bienes raíces'), ('', 'Selecciona su sector'), ('Salud', 'Salud'), ('Educación y formación', 'Educación y formación'), ('Artes y recreación', 'Artes y recreación'), ('Administración pública y seguridad', 'Administración pública y seguridad'), ('Alojamiento y alimentos', 'Alojamiento y alimentos'), ('Construcción', 'Construcción'), ('Comercio mayorista', 'Comercio mayorista'), ('Transporte, postal y almacenamiento', 'Transporte, postal y almacenamiento'), ('Medios de información y telecomunicaciones', 'Medios de información y telecomunicaciones'), ('Administración y apoyo', 'Administración y apoyo'), ('Electricidad, gas, agua y desechos', 'Electricidad, gas, agua y desechos'), ('Atención de la salud y asistencia social', 'Atención de la salud y asistencia social'), ('Profesionales, científicos y técnicos', 'Profesionales, científicos y técnicos'), ('Finanzas y seguros', 'Finanzas y seguros'), ('Comercio minorista', 'Comercio minorista'), ('Agricultura, silvicultura y pesca', 'Agricultura, silvicultura y pesca'), ('Minería', 'Minería'), ('Otros servicios', 'Otros servicios')], default='', max_length=105, null=True)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Prefiero no decirlo', 'Prefiero no decirlo'), ('Otro', 'Otro')], default='Prefiero no decirlo', max_length=30)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('sector', models.CharField(choices=[('Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería', 'Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería'), ('Obreros - Otros obreros', 'Obreros - Otros obreros'), ('Gerentes - Gerentes de hostelería, retail y servicios', 'Gerentes - Gerentes de hostelería, retail y servicios'), ('Trabajadores de ventas - Apoyo a las ventas', 'Trabajadores de ventas - Apoyo a las ventas'), ('Técnicos y trabajadores calificados - Trabajadores calificados en construcción', 'Técnicos y trabajadores calificados - Trabajadores calificados en construcción'), ('Profesionales - Profesionales de las artes y los medios', 'Profesionales - Profesionales de las artes y los medios'), ('Técnicos y trabajadores calificados - Trabajadores calificados en alimentos', 'Técnicos y trabajadores calificados - Trabajadores calificados en alimentos'), ('Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura', 'Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura'), ('Trabajadores de oficina y administrativos - Asistentes personales y secretarias', 'Trabajadores de oficina y administrativos - Asistentes personales y secretarias'), ('Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería', 'Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería'), ('Profesionales - Profesionales de TIC', 'Profesionales - Profesionales de TIC'), ('Obreros - Asistentes de preparación de alimentos', 'Obreros - Asistentes de preparación de alimentos'), ('Trabajadores de ventas - Asistentes de ventas y vendedores', 'Trabajadores de ventas - Asistentes de ventas y vendedores'), ('Profesionales - Profesionales en derecho, social y bienestar', 'Profesionales - Profesionales en derecho, social y bienestar'), ('Trabajadores de oficina y administrativos - Apoyo clerical y de oficina', 'Trabajadores de oficina y administrativos - Apoyo clerical y de oficina'), ('Gerentes - Gerentes especializados', 'Gerentes - Gerentes especializados'), ('Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas', 'Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas'), ('Profesionales - Profesionales de la salud', 'Profesionales - Profesionales de la salud'), ('', 'Selecciona su cargo'), ('Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados', 'Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados'), ('Obreros - Trabajadores de granjas, silvicultura y jardines', 'Obreros - Trabajadores de granjas, silvicultura y jardines'), ('Obreros - Obreros de construcción y minería', 'Obreros - Obreros de construcción y minería'), ('Trabajadores de oficina y administrativos - Oficinistas numéricos', 'Trabajadores de oficina y administrativos - Oficinistas numéricos'), ('Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte', 'Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte'), ('Profesionales - Profesionales en educación', 'Profesionales - Profesionales en educación'), ('Operadores de maquinaria y conductores - Operadores de plantas móviles', 'Operadores de maquinaria y conductores - Operadores de plantas móviles'), ('Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones', 'Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones'), ('Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes', 'Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar', 'Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar'), ('Obreros - Limpiadores y trabajadores de lavandería', 'Obreros - Limpiadores y trabajadores de lavandería'), ('Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas', 'Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas'), ('Profesionales - Profesionales en negocios, recursos humanos y mercadeo', 'Profesionales - Profesionales en negocios, recursos humanos y mercadeo'), ('Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril', 'Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección', 'Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección'), ('Trabajadores de ventas - Representantes y agentes de ventas', 'Trabajadores de ventas - Representantes y agentes de ventas'), ('Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias', 'Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias'), ('Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos', 'Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos'), ('Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia', 'Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia'), ('Operadores de maquinaria y conductores - Almacenistas', 'Operadores de maquinaria y conductores - Almacenistas'), ('Trabajadores de oficina y administrativos - Trabajadores clericales generales', 'Trabajadores de oficina y administrativos - Trabajadores clericales generales'), ('Obreros - Trabajadores de procesos en fábricas', 'Obreros - Trabajadores de procesos en fábricas'), ('Gerentes - Directores ejecutivos, gerentes generales y legisladores', 'Gerentes - Directores ejecutivos, gerentes generales y legisladores'), ('Gerentes - Agricultores y gerentes de granjas', 'Gerentes - Agricultores y gerentes de granjas')], default='', max_length=105, null=True)),
                ('type_user', models.CharField(choices=[('Superuser', 'Superuser'), ('User', 'User'), ('Admin', 'Admin')], default='User', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'admin',
                'verbose_name_plural': 'admins',
                'db_table': 'admins',
                'ordering': ['email', '-name'],
            },
        ),
    ]
