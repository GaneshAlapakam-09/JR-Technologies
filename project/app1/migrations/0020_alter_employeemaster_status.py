# Generated by Django 5.1.5 on 2025-01-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_materialmaster_material_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='Status',
            field=models.IntegerField(default=1),
        ),
    ]
