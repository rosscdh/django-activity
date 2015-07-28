# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import activity.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.CharField(max_length=255)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(default=activity.models._datetime)),
                ('data', jsonfield.fields.JSONField(default={})),
            ],
            options={
                'ordering': ('-timestamp',),
            },
            bases=(models.Model,),
        ),
    ]
