# Generated by Django 2.2.11 on 2020-03-24 12:57
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("api", "0002_auto_20200324_0853"),
    ]

    operations = [
        migrations.RenameModel(old_name="Item", new_name="Event",),
        migrations.RenameField(
            model_name="article", old_name="item", new_name="event",
        ),
    ]
