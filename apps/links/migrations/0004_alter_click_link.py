# Generated by Django 5.0.6 on 2024-05-30 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0003_link_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="click",
            name="link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clicks",
                to="links.link",
            ),
        ),
    ]
