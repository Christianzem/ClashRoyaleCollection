# Generated by Django 4.2.11 on 2024-05-08 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Upgraded on'),
            preserve_default=False,
        ),
    ]
