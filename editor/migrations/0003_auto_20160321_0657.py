# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import editor.models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_auto_20160320_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effect',
            name='effect',
            field=models.ImageField(max_length=255, upload_to=editor.models.get_effect_path),
        ),
    ]
