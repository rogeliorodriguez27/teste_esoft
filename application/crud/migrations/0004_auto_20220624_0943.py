# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-06-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20220623_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('price', models.PositiveIntegerField(verbose_name='pre\xe7o')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'produtos',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
