# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('college', models.ForeignKey(to='colleges.College')),
                ('department', models.ForeignKey(to='departments.Department')),
            ],
            options={
                'verbose_name_plural': 'Branches',
                'verbose_name': 'Branch',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=120, verbose_name='College Name'),
        ),
    ]
