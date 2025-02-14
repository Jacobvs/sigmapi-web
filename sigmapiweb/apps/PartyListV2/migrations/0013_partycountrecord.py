# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 17:49
from __future__ import unicode_literals

import common.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("PartyListV2", "0012_auto_20181022_0058"),
    ]

    operations = [
        migrations.CreateModel(
            name="PartyCountRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guycount", models.IntegerField()),
                ("girlcount", models.IntegerField()),
                ("guysever", models.IntegerField()),
                ("girlsever", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "party",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_party",
                        to="PartyListV2.Party",
                    ),
                ),
            ],
            bases=(common.mixins.ModelMixin, models.Model),
        ),
    ]
