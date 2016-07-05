# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cep', models.CharField(max_length=12, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=80, verbose_name='Bairro')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('cidade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.Estado'),
        ),
    ]
