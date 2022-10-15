# Generated by Django 3.0.10 on 2022-10-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0005_auto_20221011_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilereademore',
            name='left_rigth',
            field=models.CharField(choices=[('right', 'image to right'), ('left', 'image to left')], default='left', max_length=5),
        ),
        migrations.AlterField(
            model_name='profilereademore',
            name='section_type',
            field=models.CharField(choices=[('ReadMore', 'Read More'), ('GoodAt', 'Good At')], default='ReadMore', max_length=10),
        ),
    ]