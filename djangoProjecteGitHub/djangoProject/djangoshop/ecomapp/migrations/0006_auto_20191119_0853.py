# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_auto_20191119_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecomapp.CartItem'),
        ),
    ]
