# Generated by Django 4.0.1 on 2022-02-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='photos/download.jpg', null=True, upload_to='photos/'),
        ),
    ]
