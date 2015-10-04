# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='turno',
            field=models.CharField(max_length=50, choices=[(b'MANHA', 'Manh\xe3'), (b'NOITE', b'Noite')]),
        ),
    ]
