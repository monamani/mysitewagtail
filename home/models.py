from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page,Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel,
    StreamFieldPanel,InlinePanel,
    MultiFieldPanel, #tabs
    ObjectList, TabbedInterface)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from blog.models import BlogDetailPage
#to show all the fileds on api 
from wagtail.api import APIField
#add tab 

class HomePageCarouselImages(Orderable) :
    #between 1 and 2 images
    page = ParentalKey("home.HomePage", related_name ="carousel_images")
    carousel_image_bloc = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name ="+" #we will keep same name of images 
    )
    panels =  [ 
        ImageChooserPanel('carousel_image_bloc')
    ]
    api_fields =[ 
        APIField("carousel_image_bloc"),
    ]
  
class HomePage(RoutablePageMixin, Page):
    # Home page model 
    templates = "home/home_page.html"
    # the best way to put the type of pages
    subpage_types= ['blog.BlogListingPage','contact.FormPage','news.NewsPage']
    # to limit the creattion of only one Home page
    max_count = 1 
    #it s only on root page
    parent_page_type = [
        'wagtailcore.Page'
    ]
    # we will add 2 fileds body and banner title required but can be null on wordpress
    banner_title = models.CharField(max_length = 100, blank = False, null=True) 
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name ="+" #we will keep same name of images 
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name ="+"
    )

    content_stream = StreamField(
        [
            ("cta", blocks.CtaBlock())
        ],
        null = True,
        blank = True
    )
 
    #use oriented object
    def getBanner(self):
        return self.banner_title
   
    
    content_panels = Page.content_panels + [
      MultiFieldPanel([
        FieldPanel('banner_title', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'), 
      ],heading= "Banner Options"),
      # we make it outside but it s not clear soo we add MultiFieldPanel 
      # instead of InlinePanel("carousel_images"),

    ]

    sidebar_panels = [
       MultiFieldPanel([
        InlinePanel("carousel_images",max_num = 5,min_num=1, label="Image")
       ], heading= "Carousel Images"),
       StreamFieldPanel("content_stream"),
    ]

    api_fields =[
        APIField("banner_title"),
        APIField("banner_image"),
        APIField("carousel_images"),
    ]
    # to hide tabs on admin
    #promote_panels =[] 
    #settings_panels=[]
    #add tab
    edit_handler = TabbedInterface ([
       ObjectList(content_panels, heading='Content Home Page'),
       #will add another tab
       ObjectList(sidebar_panels, heading='Carousel Section'),
       ObjectList(Page.promote_panels, heading='Promotional Stuff'),
       ObjectList(Page.settings_panels, heading='Settings Stuff'),
    ])
    
    
    class Meta:
        verbose_name = "HOME PAGE"
        verbose_name_plural = "HOME PAGES"

    #render a page we create new link and put our template
    @route(r'^subscribers/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['a_special_test'] = "hello world simple varibale passed"
        return render(request,'home/subscribe.html', context)
#{'title': "hello world 12", 'cal': "hello world 12"}

#change the default title
HomePage._meta.get_field("title").verbose_name = " The title of the page"
HomePage._meta.get_field("title").help_text = None
#HomePage._meta.get_field("title").default = "Some default title"
#HomePage._meta.get_field("slug").default = "default-slug"
