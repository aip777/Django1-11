# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-29 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantslocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantslocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
    ]
