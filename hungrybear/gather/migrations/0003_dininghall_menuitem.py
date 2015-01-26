# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0002_school_menu_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiningHall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(to='gather.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_time', models.IntegerField(choices=[(1, b'breakfast'), (2, b'lunch'), (3, b'dinner'), (4, b'late night')])),
                ('last_served', models.DateField(auto_now=True)),
                ('times_served', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('dining_hall', models.ForeignKey(to='gather.DiningHall')),
                ('school', models.ForeignKey(to='gather.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
