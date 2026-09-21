from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageWithCaptionBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)

    class Meta:
        template = 'blocks/image_with_caption.html'
        icon = 'image'
        label = 'Image avec légende'


class VideoEmbedBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    url = blocks.URLBlock(help_text='URL YouTube, Vimeo ou autre vidéo intégrable')

    class Meta:
        template = 'blocks/video_embed.html'
        icon = 'media'
        label = 'Vidéo'


def rich_content_blocks():
    return [
        ('heading', blocks.CharBlock(form_classname='title', icon='title', label='Titre')),
        ('paragraph', blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link', 'ol', 'ul', 'blockquote'], label='Paragraphe')),
        ('image', ImageWithCaptionBlock()),
        ('quote', blocks.BlockQuoteBlock(label='Citation')),
        ('video', VideoEmbedBlock()),
    ]
