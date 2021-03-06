# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_id_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='user_dashboard.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='user_dashboard.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
