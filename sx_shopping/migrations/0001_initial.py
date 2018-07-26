# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sx_user', '0001_initial'),
        ('sx_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sx_store.GoodsValue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sx_user.UserModel')),
            ],
            options={
                'db_table': 'sx_cart',
            },
        ),
    ]
