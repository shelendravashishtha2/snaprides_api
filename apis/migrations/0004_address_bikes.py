# Generated by Django 3.2.6 on 2021-08-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20210811_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('landmark', models.CharField(blank=True, max_length=120, null=True)),
                ('city_name', models.CharField(max_length=30)),
                ('offer_code', models.CharField(blank=True, max_length=30, null=True)),
                ('offer_discount', models.IntegerField(blank=True, null=True)),
                ('station_start_timing', models.DateTimeField(auto_now_add=True)),
                ('station_end_timing', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_photo', models.ImageField(blank=True, null=True, upload_to='static/Bikes')),
                ('company_name', models.CharField(max_length=30)),
                ('bike_name', models.CharField(max_length=30)),
                ('curr_available', models.IntegerField(blank=True, default=0, null=True)),
                ('free_kms', models.IntegerField(blank=True, null=True)),
                ('total_price', models.IntegerField()),
                ('discount_on_price', models.IntegerField(blank=True, null=True)),
                ('bikes_availability', models.ManyToManyField(blank=True, null=True, to='apis.Address')),
            ],
        ),
    ]