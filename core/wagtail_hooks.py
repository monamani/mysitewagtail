from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/custom-admin.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/custom-admin.css")
    )


@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/css/custom-admin.js to the admin."""
    return format_html(
        '<script src="{}"></script>',
        static("/js/custom-admin.js")
    )
