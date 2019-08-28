# Generated by Django 2.2.4 on 2019-08-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0004_auto_20190822_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'Susbcriber', 'verbose_name_plural': 'Subscribers'},
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.CharField(help_text='Email address', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='full_name',
            field=models.CharField(help_text='First and last name', max_length=100),
        ),
    ]
