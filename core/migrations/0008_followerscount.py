# Generated by Django 4.2.9 on 2024-01-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_likepost"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
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
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]
