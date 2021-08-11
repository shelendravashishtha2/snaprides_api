# Generated by Django 3.2.6 on 2021-08-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20210811_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='kyc_info',
        ),
        migrations.AddField(
            model_name='users',
            name='aadhar_card_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/Document'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/Document'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
    ]