# Generated by Django 4.2.8 on 2023-12-06 11:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_article_thumbnail"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="thumbnail",
            new_name="thumb",
        ),
    ]
