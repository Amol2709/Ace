# Generated by Django 4.1.1 on 2022-09-20 22:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0002_alter_farmerinfo_district_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
