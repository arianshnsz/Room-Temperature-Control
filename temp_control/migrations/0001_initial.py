# Generated by Django 4.2.6 on 2023-10-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cooler_status", models.BooleanField(default=False)),
                ("heater_status", models.BooleanField(default=False)),
                ("is_automatic", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city_temperature", models.IntegerField()),
                ("city_weather_condition", models.CharField(max_length=200)),
            ],
        ),
    ]
