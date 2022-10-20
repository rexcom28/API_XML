# Generated by Django 3.0.10 on 2022-10-20 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0010_auto_20221015_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='profilie_social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Linkedin', 'Linkedin')], max_length=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_social', to='Profiles.Profile')),
            ],
        ),
    ]