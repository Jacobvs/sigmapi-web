# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PartyListV2", "0004_partyguest_inviteused"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="partyguest",
            name="signedIn",
        ),
        migrations.AddField(
            model_name="partyguest",
            name="_signedIn",
            field=models.BooleanField(db_column="signedIn", default=False),
        ),
        migrations.AddField(
            model_name="partyguest",
            name="cachedJSON",
            field=models.TextField(blank=True, default=""),
        ),
    ]
