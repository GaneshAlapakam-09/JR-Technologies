# Generated by Django 5.1.5 on 2025-01-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_employeemaster_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='Status',
            field=models.IntegerField(),
        ),
    ]
