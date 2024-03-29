# Generated by Django 4.2.10 on 2024-03-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_alter_services_options_alter_services_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
