# Generated by Django 3.0.10 on 2022-10-12 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0006_auto_20221011_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_title',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
