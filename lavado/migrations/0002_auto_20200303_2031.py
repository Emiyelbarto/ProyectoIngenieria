# Generated by Django 3.0.3 on 2020-03-03 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lavado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lavado',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lavadohasarticulo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lugarcompra',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='paquete',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='rolempleado',
            options={'managed': False},
        ),
    ]
