# Generated by Django 3.1.7 on 2021-05-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0020_auto_20210516_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmanagement',
            name='booking_request_log',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookingmanagement',
            name='last_chage_history',
            field=models.DateField(auto_now_add=True),
        ),
    ]
