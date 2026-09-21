# Generated manually for site branding subtitle.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_headermenusettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitebrandingsettings',
            name='subtitle',
            field=models.CharField(blank=True, default='', help_text='Texte affiché sous le grand titre de la page d’accueil.', max_length=180, verbose_name='Sous-titre'),
        ),
    ]
