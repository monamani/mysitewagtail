# streams/blocks.py
from blog.models import BlogDetailPage
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock) :
    
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')
 
    class Meta : 
        template = "streams/title_and_text_blocks.html"
        icon = "edit"
        label= "Title & Text"

class RichTextBlock(blocks.RichTextBlock) :
    """RichText with all feature """
      
    class Meta : 
        template = "streams/richtext_block.html"
        icon = "doc-full-inverse"
        label= "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock) :
    """RichText with only bold and italic """

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):   
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]
   
    class Meta : 
        template = "streams/simlerichtext_block.html"
        icon = "doc-full"
        label= "Simple RichText"

class CardBlock(blocks.StructBlock) :
    """ Crads with image and text and button"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required = True)),
                ("title", blocks.CharBlock(required=True, help_text='Title of your card', max_length=40)),
                ("text", blocks.TextBlock(required=True, help_text='Description of your card', max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,help_text = "if the button page above is selected, that will be used first")),
            ]
        )
    )
 
    class Meta : 
        template = "streams/card_blocks.html"
        icon = "snippet"
        label= "Cards "

class CtaBlock(blocks.StructBlock) :
    """ Simle call to action"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.RichTextBlock(required=True, help_text='Add your text', features = ['bold','italic'])
    button_page= blocks.PageChooserBlock(required=False, help_text='Add your page/post url')
    button_url= blocks.URLBlock(required=False, help_text='Add your Button Url')
    button_text = blocks.CharBlock(required=False, help_text='Add your button text', default ='Read more',max_length=40)

    class Meta : 
        template = "streams/cta_blocks.html"
        icon = "placeholder"
        label= "Call to action "

#NNOw if i need to get the value of button url instead of make test on the template 
#will make it here
class LinkStructValue(blocks.StructValue) : 
    #Add logic to our buttone
    def url(self) : 
        button_page = self.get('button_page')  
        button_url  = self.get('button_url')  
        if button_page : 
            return button_page.url
        elif button_url:
            return button_url.url

        return None
    #if i want to call list of blog also
    def latest_posts(self) :
        return BlogDetailPage.objects.live().public()[:2]

class ButtonBlock(blocks.StructBlock):
    """Internal or External Button URL """

    button_page= blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url= blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')
    
  
    class Meta : 
        template = "streams/button_block.html"
        icon = "link"
        label= "Single Button "
        value_class = LinkStructValue
        # we add the link value
        


   