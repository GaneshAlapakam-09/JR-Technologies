# Generated by Django 5.1.5 on 2025-02-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_alter_inwardmaster_inward_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwardmaster',
            name='Material_Id',
            field=models.CharField(max_length=55),
        ),
    ]
