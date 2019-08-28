from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks as my_blocks  #block create by me
from wagtail.core import blocks
# Create your models here.
 
class NewsPage(Page) : 
    """  News page temaple"""
    template = "news/news_page.html"
     
    # @todo add streamfields
    content_stream = StreamField(
        [
            ("title_and_text", my_blocks.TitleAndTextBlock()),
            ("full_richText",  my_blocks.RichTextBlock()),
            ("simple_richText",  my_blocks.SimpleRichTextBlock()),
            ("cards", my_blocks.CardBlock()),
            ("cta", my_blocks.CtaBlock()),
            ("button_url",my_blocks.ButtonBlock()),
            ("char_block", blocks.CharBlock(
                required=True,
                help_text='Oh wow this is help text!!',
                min_length=10,
                max_length=50,
                template="streams/char_block.html",
            ))
        ],
        null = True,
        blank = True
    )

    subtitle = models.CharField(max_length = 100 , null = True , blank = True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content_stream")
    ]

    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Pages"