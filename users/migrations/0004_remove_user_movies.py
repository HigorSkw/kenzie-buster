# Generated by Django 4.1.4 on 2022-12-08 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_movies_alter_user_is_employee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="movies",
        ),
    ]
