# Generated by Django 4.1.7 on 2023-03-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_alter_comment_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="recommend",
            field=models.BooleanField(default=True),
        ),
    ]
