# Generated by Django 3.0.10 on 2022-11-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0005_auto_20221107_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology_type',
            options={'ordering': ['tech']},
        ),
        migrations.AlterField(
            model_name='profile_work_images',
            name='data_type',
            field=models.CharField(choices=[('Javascript', 'Javascript-Javascript'), ('Python', 'Python-python'), ('Vue.js', 'Vue.js-Vue.js description\r\nmaybe can be the next project to take')], max_length=30),
        ),
        migrations.AlterField(
            model_name='profilie_social_media',
            name='social_type',
            field=models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Linkedin', 'Linkedin')], max_length=30, unique=True),
        ),
    ]
