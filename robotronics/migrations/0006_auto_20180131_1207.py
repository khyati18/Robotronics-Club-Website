# Generated by Django 2.0 on 2018-01-31 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotronics', '0005_auto_20180127_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='details',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='details',
            new_name='text',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]