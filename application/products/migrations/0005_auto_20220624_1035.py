# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-06-24 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220624_0943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['name', '-price', '-stock'], 'verbose_name': 'produtos'},
        ),
    ]
