# Generated by Django 4.1.4 on 2022-12-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_rename_orders_movie_users_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieorder",
            name="buyed_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
