# Generated by Django 3.0.5 on 2020-07-29 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
        ('registroDefectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrodefecto',
            options={'ordering': ['id_tipo_defecto', 'fecha'], 'verbose_name': 'Registro de defecto', 'verbose_name_plural': 'Registro de defectos'},
        ),
        migrations.RemoveField(
            model_name='registrodefecto',
            name='fecha_encontrado',
        ),
        migrations.RemoveField(
            model_name='registrodefecto',
            name='fecha_removido',
        ),
        migrations.AddField(
            model_name='registrodefecto',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='registrodefecto',
            name='id_programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Programa', verbose_name='Programa'),
        ),
    ]
