# Generated by Django 2.1.7 on 2019-03-28 18:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("voterroll", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="GeocodeResult",
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
                ("geocoded_address", models.CharField(max_length=300)),
                ("is_exact", models.BooleanField()),
                (
                    "coordinates",
                    django.contrib.gis.db.models.fields.PointField(
                        null=True, srid=4326
                    ),
                ),
                ("tiger_line", models.CharField(max_length=20)),
                ("tiger_side", models.CharField(max_length=2)),
                ("county_fips", models.CharField(max_length=4)),
                ("tract", models.CharField(max_length=8)),
                ("block", models.CharField(max_length=8)),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="geocodes",
                        to="voterroll.VoterRecord",
                    ),
                ),
            ],
        )
    ]
