# Generated by Django 4.2.11 on 2024-05-13 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_card_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='level',
        ),
    ]
