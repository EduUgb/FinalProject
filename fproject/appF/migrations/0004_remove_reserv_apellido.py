# Generated by Django 5.1.2 on 2024-11-16 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appF', '0003_alter_reserv_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserv',
            name='apellido',
        ),
    ]
