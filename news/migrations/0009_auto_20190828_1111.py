# Generated by Django 2.2.4 on 2019-08-28 07:11

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190825_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='content_stream',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richText', streams.blocks.RichTextBlock()), ('simple_richText', streams.blocks.SimpleRichTextBlock()), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title of your card', max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Description of your card', max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='if the button page above is selected, that will be used first', required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Add your text', required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Add your page/post url', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Add your Button Url', required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Read more', help_text='Add your button text', max_length=40, required=False))])), ('button_url', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))])), ('char_block', wagtail.core.blocks.CharBlock(help_text='Oh wow this is help text!!', max_length=50, min_length=10, required=True, template='streams/char_block.html'))], blank=True, null=True),
        ),
    ]
