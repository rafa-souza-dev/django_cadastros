# Generated by Django 3.1.7 on 2021-03-31 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20210329_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(help_text='exemplo: 22/06/2002', verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(help_text='exemplo@contato.com', max_length=36, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)], verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='observacao',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Observação'),
        ),
    ]
