# Generated by Django 2.2.11 on 2020-04-10 21:18
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0028_screenshot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="authorizer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="events",
                to="api.Authorizer",
            ),
        ),
    ]
