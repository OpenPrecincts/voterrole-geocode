# Generated by Django 2.2 on 2019-04-23 16:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("voterroll", "0008_auto_20190410_1555")]

    operations = [
        migrations.CreateModel(
            name="County",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state_fips", models.CharField(max_length=2)),
                ("county_fips", models.CharField(max_length=4)),
                ("name", models.CharField(max_length=100)),
                ("poly", django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        )
    ]
