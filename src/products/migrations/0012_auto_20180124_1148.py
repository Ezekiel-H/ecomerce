# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-24 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180119_1734'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('slug', 'supplier')]),
        ),
    ]
