# Generated by Django 5.1.2 on 2024-11-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appF', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv',
            name='codigo',
            field=models.AutoField(max_length=6, primary_key=True, serialize=False),
        ),
    ]