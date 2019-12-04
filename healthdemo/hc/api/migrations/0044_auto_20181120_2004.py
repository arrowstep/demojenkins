# Generated by Django 2.1.3 on 2018-11-20 20:04

import json

from django.db import migrations


def combine_channel_names(apps, schema_editor):
    Channel = apps.get_model("api", "Channel")
    for channel in Channel.objects.filter(kind="sms"):
        if channel.value.startswith("{"):
            doc = json.loads(channel.value)
            channel.name = doc.get("label", "")
            channel.save()


class Migration(migrations.Migration):

    dependencies = [("api", "0043_channel_name")]

    operations = [migrations.RunPython(combine_channel_names)]