# Generated by Django 5.0.7 on 2024-08-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_Api', '0006_employees_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        # migrations.AlterField(
        #     model_name='employees',
        #     name='register_by_hr',
        #     field=models.CharField(default='', max_length=20),
        # ),
    ]
