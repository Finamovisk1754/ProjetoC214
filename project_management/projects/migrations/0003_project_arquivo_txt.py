# Generated by Django 5.0.6 on 2024-06-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_created_by_project_owner_project_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='arquivo_txt',
            field=models.FileField(blank=True, null=True, upload_to='arquivos/'),
        ),
    ]
