# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-05 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("PartyListV2", "0003_partyguest_hasprepartyaccess"),
    ]

    operations = [
        migrations.AddField(
            model_name="partyguest",
            name="inviteUsed",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invites_used_for",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
