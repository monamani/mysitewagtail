# Generated by Django 2.2.4 on 2019-08-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0005_auto_20190822_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]