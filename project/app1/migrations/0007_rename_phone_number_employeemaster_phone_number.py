# Generated by Django 5.1.5 on 2025-01-22 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_employeemaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemaster',
            old_name='Phone_number',
            new_name='Phone_Number',
        ),
    ]
