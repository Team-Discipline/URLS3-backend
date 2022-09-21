# Generated by Django 4.1.1 on 2022-09-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_rename_captureduserdata_captureddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='captureddata',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='captureddata',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='captureddata',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='captureddata',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]