# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PartyListV2", "0007_auto_20180510_2347"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="restrictedguest",
            options={
                "default_permissions": [],
                "permissions": (
                    ("view_restricted_guests", "Can view Restricted Guests"),
                    ("manage_blacklist", "Can manage the Blacklist"),
                    ("add_graylist", "Can add to the Graylist"),
                    ("manage_graylist", "Can manage any Graylisted Guest"),
                ),
            },
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="_signedIn",
            new_name="_signed_in",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="addedBy",
            new_name="added_by",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="createdAt",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="everSignedIn",
            new_name="ever_signed_in",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="hasPrepartyAccess",
            new_name="has_preparty_access",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="inviteUsed",
            new_name="invite_used",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="timeFirstSignedIn",
            new_name="time_first_signed_in",
        ),
        migrations.RenameField(
            model_name="partyguest",
            old_name="wasVouchedFor",
            new_name="was_vouched_for",
        ),
        migrations.RemoveField(
            model_name="partyguest",
            name="cachedJSON",
        ),
    ]
