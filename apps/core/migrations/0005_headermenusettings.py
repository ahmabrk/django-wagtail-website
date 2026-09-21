# Generated manually for header menu settings.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_sitebrandingsettings_options'),
        ('wagtailcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderMenuSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_label', models.CharField(default='blog', max_length=80, verbose_name='Texte du premier lien')),
                ('first_url', models.CharField(default='/blog/', max_length=255, verbose_name='URL du premier lien')),
                ('second_label', models.CharField(default='books', max_length=80, verbose_name='Texte du deuxième lien')),
                ('second_url', models.CharField(default='/livres/', max_length=255, verbose_name='URL du deuxième lien')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Menu du haut',
                'verbose_name_plural': 'Menu du haut',
            },
        ),
    ]
