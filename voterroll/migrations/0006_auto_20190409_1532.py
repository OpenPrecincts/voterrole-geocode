# Generated by Django 2.1.7 on 2019-04-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voterroll', '0005_auto_20190409_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterrecord',
            name='latest_geocode_result',
            field=models.CharField(choices=[('G', 'Geocoded'), ('X', 'No Result From Geocoder'), (' ', 'No Attempt')], default=' ', max_length=1),
        ),
        migrations.AddField(
            model_name='voterrecord',
            name='latest_geocode_time',
            field=models.DateTimeField(null=True),
        ),
    ]
