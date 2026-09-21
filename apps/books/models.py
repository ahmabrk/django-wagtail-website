from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from apps.core.blocks import rich_content_blocks


class BooksIndexPage(Page):
    intro = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [FieldPanel('intro')]
    subpage_types = ['books.BookPage']

    def get_context(self, request):
        context = super().get_context(request)
        books = BookPage.objects.live().descendant_of(self).order_by('title')
        context['books'] = books
        return context


class BookPage(Page):
    EBOOK = 'ebook'
    PAPER = 'paper'
    BOTH = 'both'
    BOOK_TYPES = [
        (EBOOK, 'Ebook'),
        (PAPER, 'Livre papier'),
        (BOTH, 'Ebook + papier'),
    ]

    intro = models.CharField(max_length=255, blank=True)
    cover_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    book_type = models.CharField(max_length=20, choices=BOOK_TYPES, default=EBOOK)
    isbn = models.CharField(max_length=64, blank=True)
    pdf_file = models.ForeignKey(
        'wagtaildocs.Document', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        help_text='PDF privé ou extrait du livre. La logique de téléchargement sécurisé sera ajoutée avec la partie paiement.',
    )
    body = StreamField(rich_content_blocks(), blank=True, use_json_field=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.FilterField('book_type'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('cover_image'),
        MultiFieldPanel([
            FieldPanel('price'),
            FieldPanel('book_type'),
            FieldPanel('isbn'),
            FieldPanel('pdf_file'),
        ], heading='Informations livre'),
        FieldPanel('body'),
    ]

    parent_page_types = ['books.BooksIndexPage']
    subpage_types = []
