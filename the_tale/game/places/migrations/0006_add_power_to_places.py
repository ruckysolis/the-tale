# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-26 12:39
from __future__ import unicode_literals

import json

from django.db import migrations


def add_political_power(apps, schema_editor):
    for person in apps.get_model("places", "Place").objects.all().iterator():
        data = json.loads(person.data)

        data['politic_power'] = {'outer_power': 5000000,
                                 'inner_power': 500000,
                                 'inner_circle': {}}

        person.data = json.dumps(data, ensure_ascii=True)

        person.save()




class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20160319_1713'),
    ]

    operations = [
        migrations.RunPython(add_political_power)
    ]
