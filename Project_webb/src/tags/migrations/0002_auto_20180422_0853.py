# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('title', 'id'), 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0432 \u0430\u0440\u0445\u0438\u0432\u0435'),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
