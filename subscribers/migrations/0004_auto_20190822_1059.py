# Generated by Django 2.2.4 on 2019-08-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_auto_20190822_1049'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscribers',
        ),
    ]