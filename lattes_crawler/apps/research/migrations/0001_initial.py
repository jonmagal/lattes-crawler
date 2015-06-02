# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('year', models.PositiveIntegerField(blank=True)),
                ('data_type', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lattes_information', picklefield.fields.PickledObjectField(null=True, editable=False)),
                ('lattes_id', models.CharField(max_length=30)),
                ('update', models.DateTimeField(auto_now=True)),
                ('collaborators', models.ManyToManyField(related_name='collaborators_rel_+', null=True, to='research.Research')),
                ('information', models.ForeignKey(to='research.Info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='info',
            name='researcher',
            field=models.ForeignKey(to='research.Research'),
            preserve_default=True,
        ),
    ]
