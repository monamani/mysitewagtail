# Generated by Django 2.2.4 on 2019-08-21 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepagecarouselimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagecarouselimages',
            old_name='carousel_image',
            new_name='carousel_image_bloc',
        ),
    ]
