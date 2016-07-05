# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('especialidades', '0002_auto_20160701_2000'),
        ('pessoas', '0001_initial'),
        ('estabelecimentos', '0004_auto_20160701_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.Pessoa')),
                ('codConselho', models.CharField(max_length=10, verbose_name='Codigo do Conselho')),
                ('urlImgProficional', models.CharField(max_length=10)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('especialidade', models.ManyToManyField(to='especialidades.Especialidade')),
                ('local', models.ManyToManyField(to='estabelecimentos.Local', verbose_name='Local de Atendimento')),
            ],
            options={
                'verbose_name': 'Profissional',
                'verbose_name_plural': 'Profissionais',
                'ordering': ['nome', 'sobrenome'],
            },
            bases=('pessoas.pessoa',),
        ),
    ]
