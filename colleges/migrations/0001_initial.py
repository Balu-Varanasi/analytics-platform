# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120, verbose_name='Name of the College')),
                ('code', models.CharField(max_length=10, verbose_name='College Code')),
            ],
            options={
                'verbose_name': 'College',
                'verbose_name_plural': 'Colleges',
            },
            bases=(models.Model,),
        ),
    ]
