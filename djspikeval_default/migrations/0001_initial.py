# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djspikeval', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultDefault',
            fields=[
                ('result_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djspikeval.Result')),
                ('file', models.ImageField(upload_to='results_default')),
                ('kind', models.IntegerField(default=0, choices=[(0, 'unknown'), (10, 'wf_single'), (20, 'wf_all'), (30, 'clus12'), (40, 'clus34'), (50, 'clus_proj'), (60, 'spiketrain')])),
            ],
            options={
            },
            bases=('djspikeval.result',),
        ),
    ]
