# Generated by Django 2.2.11 on 2020-03-24 14:47
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_auto_20200324_1045"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="recovered",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
