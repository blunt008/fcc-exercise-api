# Generated by Django 3.0.5 on 2020-04-25 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200425_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
