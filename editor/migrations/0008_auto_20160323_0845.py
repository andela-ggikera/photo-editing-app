# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import editor.models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0007_auto_20160323_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_effect',
            field=models.FileField(max_length=255, null=True, upload_to=editor.models.get_effect_path),
        ),
    ]
