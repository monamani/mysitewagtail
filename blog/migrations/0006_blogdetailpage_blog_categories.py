# Generated by Django 2.2.4 on 2019-08-25 09:42

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage',
            name='blog_categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]