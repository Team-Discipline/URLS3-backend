# Generated by Django 4.1.4 on 2022-12-22 06:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='captureddata',
            old_name='js_reqeust_time_UTC',
            new_name='js_request_time_UTC',
        ),
    ]
