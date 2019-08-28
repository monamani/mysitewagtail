from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.views import generic
from .models import BlogListingPage ,BlogDetailPage
"""
For django we use views  but wagtail combinate both views + models
class BlogList(generic.ListView):
    queryset = BlogListingPage.objects.all()
    template_name = 'blog/blog_index_page.html'
    paginate_by = 1

class BlogDetail(generic.DetailView):
    model = BlogDetailPage
    template_name = 'blog/blog_page.html'

"""
 