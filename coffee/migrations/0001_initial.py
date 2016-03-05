# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type_of_drink', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date made')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='order',
            field=models.ForeignKey(to='coffee.Order'),
        ),
    ]
