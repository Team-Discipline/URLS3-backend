# Generated by Django 4.1.6 on 2023-02-19 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("S3", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CapturedData",
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
                ("ip_address", models.GenericIPAddressField()),
                ("js_request_time_UTC", models.DateTimeField()),
                ("page_loaded_time", models.DateTimeField()),
                ("page_leave_time", models.DateTimeField()),
                ("referer_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("country", models.CharField(blank=True, max_length=1000, null=True)),
                ("city", models.CharField(blank=True, max_length=1000, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                (
                    "s3",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="captured_data",
                        to="S3.s3",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="UniqueVisitor",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="unique_visitors",
                        to="analytics.captureddata",
                    ),
                ),
            ],
        ),
    ]
