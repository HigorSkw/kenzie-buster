# Generated by Django 4.1.4 on 2022-12-12 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_movie_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="owner",
            new_name="user",
        ),
    ]