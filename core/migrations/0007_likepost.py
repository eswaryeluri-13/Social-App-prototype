# Generated by Django 4.2.9 on 2024-01-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
    ]
