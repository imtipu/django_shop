# Generated by Django 2.2.12 on 2020-09-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200922_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customershippingaddress',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=17),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=17),
        ),
    ]