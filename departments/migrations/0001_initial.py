# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='Department Name')),
                ('code', models.CharField(max_length=10, verbose_name='Department Code')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'verbose_name': 'Department',
            },
            bases=(models.Model,),
        ),
    ]
