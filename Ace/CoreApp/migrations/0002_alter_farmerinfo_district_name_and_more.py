# Generated by Django 4.1.1 on 2022-09-20 09:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerinfo',
            name='district_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='state_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='text_column_1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='text_column_2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='text_column_3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='text_column_4',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='farmerinfo',
            name='village_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
