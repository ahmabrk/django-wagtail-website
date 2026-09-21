# Generated manually for the starter project.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0001_initial'),
        ('wagtailimages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBrandingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name_first', models.CharField(default='ABC', max_length=80, verbose_name='Nom du site - première partie')),
                ('site_name_second', models.CharField(default='ABC', max_length=80, verbose_name='Nom du site - deuxième partie')),
                ('subtitle', models.CharField(blank=True, default='', help_text='Texte affiché sous le grand titre de la page d’accueil.', max_length=180, verbose_name='Sous-titre')),
                ('logo_image', models.ForeignKey(blank=True, help_text='Image affichée à gauche du titre. Si vide, une image par défaut est utilisée.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Symbole / logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
