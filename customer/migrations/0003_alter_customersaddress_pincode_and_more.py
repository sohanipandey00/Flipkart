# Generated by Django 4.2.1 on 2023-05-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customersaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersaddress',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customersaddress',
            name='street_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]