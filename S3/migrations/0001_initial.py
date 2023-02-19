# Generated by Django 4.1.6 on 2023-02-19 13:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CombinedWord",
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
            ],
            options={
                "verbose_name": "CombinedWord",
                "verbose_name_plural": "CombinedWords",
            },
        ),
        migrations.CreateModel(
            name="Hash",
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
                (
                    "target_url",
                    models.URLField(validators=[django.core.validators.URLValidator]),
                ),
                ("hash_value", models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name="S3SecurityResult",
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
                ("has_hsts", models.BooleanField()),
            ],
            options={
                "verbose_name": "Security Result",
                "verbose_name_plural": "Security Results",
            },
        ),
        migrations.CreateModel(
            name="Word",
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
                ("word", models.CharField(max_length=100, unique=True)),
                ("is_noun", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="S3",
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
                (
                    "target_url",
                    models.URLField(validators=[django.core.validators.URLValidator]),
                ),
                (
                    "s3_url",
                    models.URLField(
                        unique=True, validators=[django.core.validators.URLValidator]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_ban", models.BooleanField(default=False)),
                (
                    "combined_words",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="s3",
                        to="S3.combinedword",
                    ),
                ),
                (
                    "hashed_value",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hash",
                        related_query_name="s3",
                        to="S3.hash",
                    ),
                ),
                (
                    "issuer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issued_s3",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "security_result",
                    models.OneToOneField(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="s3",
                        to="S3.s3securityresult",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="combinedword",
            name="first_word",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="first_words",
                to="S3.word",
            ),
        ),
        migrations.AddField(
            model_name="combinedword",
            name="second_word",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="second_words",
                to="S3.word",
            ),
        ),
    ]
