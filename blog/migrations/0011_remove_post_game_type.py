# Generated by Django 5.0.2 on 2024-04-06 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_game_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='game_type',
        ),
    ]