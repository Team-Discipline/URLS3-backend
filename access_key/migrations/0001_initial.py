# Generated by Django 4.1.6 on 2023-02-19 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rest_framework_api_key", "0005_auto_20220110_1102"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UsualAPIKey",
            fields=[
                (
                    "apikey_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="rest_framework_api_key.apikey",
                    ),
                ),
                ("key", models.CharField(max_length=1000)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "API key",
                "verbose_name_plural": "API keys",
                "ordering": ("-created",),
                "abstract": False,
            },
            bases=("rest_framework_api_key.apikey",),
        ),
    ]
