# Generated by Django 3.1.7 on 2021-06-28 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeMeet', '0002_auto_20210627_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='school_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_batch', to='WeMeet.school'),
        ),
    ]