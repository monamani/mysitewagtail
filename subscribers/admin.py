from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Subscribers

class SubscribersAdmin(ModelAdmin):
    #Subscriber admin. 
    model = Subscribers
    menu_label = 'Subscribers'  # ditch this to use verbose_name_plural from model
    menu_icon = 'mail'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('email', 'full_name')
    list_filter = ('email',)
    search_fields = ('email', 'full_name') 

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(SubscribersAdmin)