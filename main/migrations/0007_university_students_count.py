# Generated by Django 4.0.2 on 2022-02-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='students_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
