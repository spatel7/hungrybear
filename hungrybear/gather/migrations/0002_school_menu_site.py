# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='menu_site',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
    ]
