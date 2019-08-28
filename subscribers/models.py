from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel
 
class Subscribers(models.Model):
    # subscriber model 
    email = models.CharField(max_length=255,help_text="Email address")
    full_name = models.CharField(max_length=255)

    panels =  [
        MultiFieldPanel([
        FieldPanel('email'),
        FieldPanel('full_name'), 
      ],heading= "Subscriber details"),
    ]


    def __str__(self):
        return self.full_name
 
    class Meta:  # noqa
        verbose_name = "Susbcriber"
        verbose_name_plural = "Subscribers"