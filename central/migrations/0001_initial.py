# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crianca', models.CharField(max_length=255, verbose_name=b'Nome da crian\xc3\xa7a')),
                ('responsavel', models.CharField(max_length=255, verbose_name=b'Nome do respons\xc3\xa1vel')),
                ('telefone', models.CharField(max_length=25)),
                ('n_ficha', models.IntegerField()),
                ('ativo', models.BooleanField(default=False)),
                ('criado_em', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Fichas',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255, verbose_name=b'Nome da Sala')),
                ('turno', models.CharField(max_length=50, choices=[(b'MANH\xc3\x83', b'Manh\xc3\xa3'), (b'NOITE', b'Noite')])),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.AddField(
            model_name='ficha',
            name='sala',
            field=models.ForeignKey(to='central.Sala'),
        ),
    ]
