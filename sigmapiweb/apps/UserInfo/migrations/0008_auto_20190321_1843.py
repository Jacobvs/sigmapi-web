# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserInfo", "0007_change_on_delete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="graduationYear",
            field=models.PositiveIntegerField(default=2022),
        ),
    ]
