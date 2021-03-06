# Generated by Django 3.2 on 2021-05-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_no', models.CharField(max_length=100)),
                ('car_capacity', models.IntegerField()),
                ('car_price', models.FloatField()),
                ('car_luggage_capa', models.IntegerField()),
                ('car_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
