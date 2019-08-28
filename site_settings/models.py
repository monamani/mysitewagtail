from django.db import models
from wagtail.admin.edit_handlers import  MultiFieldPanel,FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    #social media settings urls
    facebook = models.URLField(blank = True, null= True,help_text="Facebook URL")
    twitter = models.URLField(blank = True, null= True,help_text="Twitter URL")
    instagram = models.URLField(blank = True, null= True,help_text="Instagram URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram")
        ], heading = "Social Media Settings")
    ]