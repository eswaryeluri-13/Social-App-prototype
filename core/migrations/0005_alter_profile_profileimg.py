# Generated by Django 4.2.9 on 2024-01-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_profile_profileimg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profileimg",
            field=models.ImageField(
                default="blank-profile-picture.png", upload_to="profile_images"
            ),
        ),
    ]
