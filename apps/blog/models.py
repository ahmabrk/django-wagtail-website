from django.db import models
from django.utils import timezone
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from apps.core.blocks import rich_content_blocks


class BlogIndexPage(Page):
    intro = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['blog.BlogPage']

    def get_context(self, request):
        context = super().get_context(request)
        posts = BlogPage.objects.live().descendant_of(self).order_by('-first_published_at')
        context['posts'] = posts
        return context


class BlogPage(Page):
    date = models.DateField(default=timezone.now)
    intro = models.CharField(max_length=255, blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField(rich_content_blocks(), blank=True, use_json_field=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('intro'),
            FieldPanel('main_image'),
        ], heading='Informations article'),
        FieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
