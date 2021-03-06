# Generated by Django 3.1.7 on 2021-03-30 01:57

import cadastro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(default=cadastro.models.nome_aleatorio, max_length=20),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(default=cadastro.models.sobrenome_aleatorio, max_length=15),
        ),
    ]
