from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.core.blocks import rich_content_blocks


class HomePage(Page):
    intro = models.CharField(
        max_length=255,
        blank=True,
        help_text='Phrase courte affichée sous le titre, si le sous-titre global est vide.',
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image optionnelle. La page d’accueil affiche surtout les derniers livres et articles.',
    )
    body = StreamField(rich_content_blocks(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('hero_image'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # Import local pour éviter les imports circulaires au démarrage de Django.
        from apps.books.models import BookPage
        from apps.blog.models import BlogPage

        context['latest_books'] = BookPage.objects.live().public().order_by('-first_published_at')[:3]
        context['latest_posts'] = BlogPage.objects.live().public().order_by('-first_published_at')[:6]
        return context
