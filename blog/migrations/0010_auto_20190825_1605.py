# Generated by Django 2.2.4 on 2019-08-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190825_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Post date'),
        ),
    ]
