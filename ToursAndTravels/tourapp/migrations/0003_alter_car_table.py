# Generated by Django 3.2 on 2021-05-12 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0002_alter_car_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='car',
            table='travels',
        ),
    ]
