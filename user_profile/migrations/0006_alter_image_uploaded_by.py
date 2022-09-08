# Generated by Django 4.1.1 on 2022-09-08 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0005_alter_image_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_image',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]