# Generated by Django 5.1.2 on 2024-11-24 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appF', '0004_remove_reserv_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserv',
            name='mesa',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
