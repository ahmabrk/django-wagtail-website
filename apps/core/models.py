from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from django.core.validators import FileExtensionValidator


@register_setting
class SiteBrandingSettings(BaseSiteSetting):
    """Paramètres modifiables depuis Wagtail > Settings > Site branding."""

    site_name = models.CharField(
        max_length=160,
        default='Site name',
        verbose_name='Nom du site',
    )
    logo_svg = models.FileField(
        upload_to='site-branding/',
        blank=True,
        validators=[FileExtensionValidator(['svg'])],
        verbose_name='Logo SVG',
        help_text='Logo SVG affiché à gauche du titre.',
    )
    subtitle = models.CharField(
        max_length=180,
        blank=True,
        default='',
        verbose_name='Sous-titre',
        help_text='Texte affiché sous le grand titre de la page d’accueil.',
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('site_name'),
            FieldPanel('logo_svg'),
            FieldPanel('subtitle'),
        ], heading='Identité du site'),
    ]

    class Meta:
        verbose_name = 'Identité du site'
        verbose_name_plural = 'Identité du site'


@register_setting(icon='list-ul')
class HeaderMenuSettings(BaseSiteSetting):
    """Liens modifiables depuis Wagtail > Paramètres > Menu du haut."""

    first_label = models.CharField(
        max_length=80,
        default='blog',
        verbose_name='Texte du premier lien',
    )
    first_url = models.CharField(
        max_length=255,
        default='/blog/',
        verbose_name='URL du premier lien',
    )
    second_label = models.CharField(
        max_length=80,
        default='book',
        verbose_name='Texte du deuxième lien',
    )
    second_url = models.CharField(
        max_length=255,
        default='/livres/',
        verbose_name='URL du deuxième lien',
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('first_label'),
            FieldPanel('first_url'),
            FieldPanel('second_label'),
            FieldPanel('second_url'),
        ], heading='Liens du menu principal'),
    ]

    class Meta:
        verbose_name = 'Menu du haut'
        verbose_name_plural = 'Menu du haut'
