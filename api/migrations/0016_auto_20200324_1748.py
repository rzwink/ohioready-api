# Generated by Django 2.2.11 on 2020-03-24 21:48
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_auto_20200324_1737"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="authoritative_url",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
