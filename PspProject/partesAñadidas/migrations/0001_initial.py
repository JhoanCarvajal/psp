# Generated by Django 3.0.5 on 2020-07-26 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0003_fase_tamañoitem_tiposdefecto_tiposparte'),
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartesAñadida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('items_planeados', models.IntegerField(verbose_name='Items planeados')),
                ('tamaño_planeado', models.IntegerField(verbose_name='Tamaño planeado')),
                ('items_acuales', models.IntegerField(verbose_name='Items actuales')),
                ('tamaño_actual', models.IntegerField(verbose_name='Tamaño actual')),
                ('id_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Programa', verbose_name='proyecto')),
                ('id_tamaño_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.TamañoItem', verbose_name='Tamaño de items')),
                ('id_tipo_parte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.TiposParte', verbose_name='Tipo de parte')),
            ],
            options={
                'verbose_name': 'PartesAñadida',
                'verbose_name_plural': 'PartesAñadidas',
                'ordering': ['nombre'],
            },
        ),
    ]
