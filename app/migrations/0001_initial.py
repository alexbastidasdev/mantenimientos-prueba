# Generated by Django 3.1.2 on 2022-09-20 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('dependencia', models.CharField(max_length=50)),
                ('periodicidad_mantenimiento', models.IntegerField()),
                ('proximo_mantenimiento', models.DateField()),
                ('estado_equipo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_manteniento', models.CharField(max_length=50)),
                ('fecha_mantenimiento', models.DateField(auto_now_add=True)),
                ('observaciones', models.TextField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipo')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tecnico')),
            ],
        ),
    ]