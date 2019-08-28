from django.db import models
from django import forms
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import render
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page,Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class BlogAuthorsOrderable(Orderable) :
    #selct 1 or more blog author from snippets
    page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
    author = models.ForeignKey(
        "blog.BlogAuthor", 
         on_delete=models.CASCADE
    )
    panels= [
        SnippetChooserPanel("author")  #instead of fieldpanel we use snipperbecuase we add as snippet 
    ]


#List of snippets 
class BlogAuthor(models.Model) : 
    #Blog author for snippets
    name = models.CharField(max_length = 100)
    website =  models.URLField(blank=True, null=True, max_length=200)
    image = models.ForeignKey(
        "wagtailimages.Image",   
        on_delete=models.SET_NULL,
        null= True,
        blank= False,
        related_name ="+")

    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            FieldPanel("website"),
            ImageChooserPanel("image")
        ],
           heading = "Author Name & image"
        ),
        MultiFieldPanel([
            FieldPanel("website"),
        ],
          heading= "Links"
        )  
    ]

    def __str__(self):
        #strinf repres of this class is then name
        return self.name
    
    class Meta :
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)



class BlogCategory(models.Model) : 
    #Blog category for a snippets
    name = models.CharField(max_length = 100)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode = True,
        max_length = 255,
        help_text = "A slug to identify posts by this category"
    )
 
    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            FieldPanel("slug"), 
        ],
           heading = "Category Name & Slug"
        )  
    ]
   
   #what it will shown on the admin page Title
    def __str__(self):
        #strinf repres of this class is then name
        return self.name
    
    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

register_snippet(BlogCategory)

class BlogListingPage(RoutablePageMixin, Page):

    template ='blog/blog_listing_page.html'
    ajax_templae = "blog/blog_listing_page_ajax.html"
    max_count = 1 
    subpage_types= ['blog.ArticleBlogPage','blog.VideoBlogPage','blog.BlogDetailPage']
    #listing all the blogs
    intro = RichTextField(blank=True)
    custom_title = models.CharField(max_length = 100,blank=False,null=False,help_text='The default page title')
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('custom_title', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        number_of_post_by_page = 4
        all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')

        #tags 
        if request.GET.get('tag', None):
           tags = request.GET.get('tag')
           all_posts = all_posts.filter(tags__slug__in=[tags])
           
        paginator= Paginator(all_posts, number_of_post_by_page)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try :
              # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger :
             # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage: 
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['blog_categories'] = BlogCategory.objects.all() 
        return context

    #/blog/category
    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view (self, request, cat_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)
        print(cat_slug)
        print(cat_slug)
      
        try:
            # Look for the blog category by its slug.
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            # Blog category doesnt exist (ie /blog/category/missing-category/)
            # Redirect to self.url, return a 404.. that's up to you!
            category = None

        if category is None:
            # This is an additional check.
            # If the category is None, do something. Maybe default to a particular category.
            # Or redirect the user to /blog/ ¯\_(ツ)_/¯
            pass
        print(category)
        print(category)
        print(category)
        context["posts"] = BlogDetailPage.objects.live().public().filter(blog_categories__in=[category]) 
        return render(request, "blog/blog_listing_page.html", context)

   # @route(r"^year/(\d+)/(\d+)/$", name="blogs_by_year")
   # def blogs_by_year(self, request, year=None, month=None):
   #     context = self.get_context(request)
        # Implement your BlogDetailPage filter. Maybe something like this:
        #if year is not None and month is not None:
        #    posts = BlogDetailPage.objects.live().public().filter(year=year, month=month)
        #else:
        #     # No year and no month were set, assume this is july-2019 only posts
    #    posts = BlogDetailPage.objects.live().public().filter(year=2019)
        # print(year)
        # print(month)
    #    context["posts"] = posts

        # Note: The below template (latest_posts.html) will need to be adjusted
    #   return render(request, "blog/blog_listing_page.html", context)
   
    # when we called on html we will call the function name
    # or we add anme to route and called throught the route name
    @route(r'^latest/$', name="latest_blog_list")
    def latest_blog(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['posts'] = context['posts'][:1] # because we already override the context
        context['isLatest'] = "My latest blog"
        return render(request,'blog/blog_listing_page.html', context)
   #we need it to add for each route

    def get_sitemap_urls(self,request) :
        # return [] if u want to hide the page sitemap
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
          { 
            "location" : self.full_url + self.reverse_subpage("latest_blog_list"),
            "lastmod" :(self.last_published_at or self.latest_revision_created_at)
          }
        ) 
        return sitemap
       

# Keep the definition of BlogIndexPage, and add:


class BlogPageTag (TaggedItemBase) :
    content_object = ParentalKey(
        'BlogDetailPage',
        related_name = "tagged_items",
        on_delete=models.CASCADE
    )


class BlogDetailPage(Page):
  # Parental Blog detail page 
    template ='blog/blog_detail.html'
    subpage_types= []
    tags = ClusterTaggableManager(through = BlogPageTag, blank = True)
    #List of fields
    date = models.DateField("Post date",blank=True,null = True)
    intro = models.CharField(max_length=250,blank=True,null = True)
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name ="+" #we will keep same name of images 
    )
    
    blog_categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('date'),
        FieldPanel('intro'),
        MultiFieldPanel([
            InlinePanel("blog_authors", label ="Author ",min_num = 0, max_num = 2),   
        ],  
         heading = "Authors(s)"
        ),
        MultiFieldPanel([
            FieldPanel("blog_categories", widget = forms.CheckboxSelectMultiple),   
        ],  
         heading = "Categories"
        ),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('banner_image'),
    ]
    # we add the save method bc when we put blog on cache and then we change it will not appear
    # so we need to override and said that there are change
    def save(self, *args, **Kwargs):
        print('------------')
        print('------Hello MOUNA i will change the cache bz you update one blog----') 
        print('------------')
        key = make_template_fragment_key(
            "blog_post_preview",
            [self.id]
        ) #self.id is the post id 
        cache.delete(key)
        return super().save(*args, **Kwargs)

#first sub class of blog post page

class ArticleBlogPage(BlogDetailPage) : 
    #a subclassed blog post page for articles
    template = "blog/article_blog_page.html"

    subtitle = models.CharField(max_length=50,blank = True, null = True)
    intro_image = models.ForeignKey(
        "wagtailimages.Image",  
        blank = True,
        null= True,
        help_text="Best size is 100x100",
        on_delete=models.SET_NULL
    )
    
    content_panels = BlogDetailPage.content_panels + [ 
         #call all the blog field + add the one for articles
        MultiFieldPanel([
            FieldPanel("subtitle"),   
            ImageChooserPanel('intro_image'),
        ],  
         heading = "Article Details"
        ), 
    ]

#Second sub class of blog post page

class VideoBlogPage(BlogDetailPage) : 
    #a subclassed blog post page for articles
    template = "blog/video_blog_page.html"
    
    youtube_video_id = models.CharField(max_length=50,blank = True, null = True)
    
    content_panels = BlogDetailPage.content_panels + [ 
        #call all the blog field + add the one for articles
        MultiFieldPanel([
            FieldPanel("youtube_video_id"),    
        ],  
         heading = "Video Details"
        ), 
    ]

