# Generated by Django 3.1.7 on 2021-07-06 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeMeet', '0006_auto_20210705_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='batch_propic',
        )
    ]
