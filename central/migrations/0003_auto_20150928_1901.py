# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_auto_20150926_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='n_ficha',
            field=models.IntegerField(verbose_name=b'N\xc3\xbamero da Ficha'),
        ),
        migrations.AlterField(
            model_name='sala',
            name='turno',
            field=models.CharField(max_length=50, choices=[('MANH\xc3', 'Manh\xe3'), (b'NOITE', b'Noite')]),
        ),
    ]
