# Generated by Django 5.0.7 on 2024-08-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_Api', '0010_rename_register_by_hr_employees_registered_by_hr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
