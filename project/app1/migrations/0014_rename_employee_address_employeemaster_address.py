# Generated by Django 5.1.5 on 2025-01-25 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_address_employeemaster_employee_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemaster',
            old_name='Employee_Address',
            new_name='Address',
        ),
    ]
