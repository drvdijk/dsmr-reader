# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_datalogger', '0003_telegram_checksum'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsmrreading',
            name='phase_currently_delivered_l1',
            field=models.DecimalField(decimal_places=3, default=None, help_text='Instantaneous active power L1 (+P) in W resolution', max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='dsmrreading',
            name='phase_currently_delivered_l2',
            field=models.DecimalField(decimal_places=3, default=None, help_text='Instantaneous active power L2 (+P) in W resolution', max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='dsmrreading',
            name='phase_currently_delivered_l3',
            field=models.DecimalField(decimal_places=3, default=None, help_text='Instantaneous active power L3 (+P) in W resolution', max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='dataloggersettings',
            name='track_phases',
            field=models.BooleanField(default=False, help_text='Whether we should track your phases (if any) as well. By default you only have one phase, but some meters have three due to solar panels or an electric stove. This feature is only useful (and will only work) when actually you have three phases. The dashboard will display any data read, after enabling this.', verbose_name='Track electricity phases'),
        ),
    ]
