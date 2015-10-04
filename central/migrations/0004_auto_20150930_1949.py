# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_auto_20150928_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='slug',
            field=models.SlugField(max_length=255, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='slug',
            field=models.SlugField(max_length=255, editable=False, blank=True),
        ),
    ]
