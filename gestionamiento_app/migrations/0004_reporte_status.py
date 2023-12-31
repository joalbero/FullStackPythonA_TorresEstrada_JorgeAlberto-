# Generated by Django 4.2.1 on 2023-06-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionamiento_app', '0003_rename_calle_reporte_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='status',
            field=models.CharField(choices=[('Pendiente por investigar', 'Pendiente por investigar'), ('Investigando', 'Investigando'), ('Trabajando en ello', 'Trabajando en ello'), ('Solucionado', 'Solucionado')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
