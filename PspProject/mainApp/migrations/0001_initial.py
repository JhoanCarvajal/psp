# Generated by Django 3.0.5 on 2020-07-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronimo', models.CharField(max_length=20, verbose_name='Acronimo')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Medida',
                'verbose_name_plural': 'Medidas',
                'ordering': ['nombre'],
            },
        ),
    ]
