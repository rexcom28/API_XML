# Generated by Django 3.0.10 on 2022-10-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0015_profile_good_at_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mywork_bio',
            field=models.TextField(blank=True),
        ),
    ]