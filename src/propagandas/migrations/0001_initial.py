# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissionais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propaganda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
                ('ativa', models.BooleanField(verbose_name='Prop. Ativa')),
                ('urlImgPropaganda', models.CharField(max_length=10, verbose_name='Numero')),
                ('proficional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profissionais.Profissional')),
            ],
        ),
    ]
