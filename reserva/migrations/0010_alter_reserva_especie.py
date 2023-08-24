# Generated by Django 4.2.1 on 2023-07-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0009_alter_reserva_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='especie',
            field=models.IntegerField(choices=[(0, 'Gato'), (1, 'Cachorro'), (2, 'Outro')], default=2, verbose_name='Espécie'),
            preserve_default=False,
        ),
    ]
