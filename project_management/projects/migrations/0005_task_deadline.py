# Generated by Django 5.0.6 on 2024-06-27 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_arquivo_txt_responsefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 27, 0, 39, 8, 877077, tzinfo=datetime.timezone.utc)),
        ),
    ]
