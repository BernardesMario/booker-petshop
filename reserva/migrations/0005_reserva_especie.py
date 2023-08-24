# Generated by Django 4.2.1 on 2023-06-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_reserva_observacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='especie',
            field=models.IntegerField(choices=[(0, 'Gato'), (1, 'Cachorro'), (2, 'Outro')], default=0, verbose_name='Espécie'),
            preserve_default=False,
        ),
    ]
