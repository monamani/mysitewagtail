# Generated by Django 2.2.4 on 2019-08-21 06:43

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newspage_content_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='content_stream',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richText', streams.blocks.RichTextBlock()), ('simple_richText', streams.blocks.SimpleRichTextBlock())], blank=True, null=True),
        ),
    ]