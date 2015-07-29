from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('Nazwa'))
    slug = models.SlugField(max_length=20, unique=True, verbose_name=_('Nazwa w'
        ' URL'))

    class Meta:
        verbose_name = _('kategoria')
        verbose_name_plural = _('kategorie')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki:category', kwargs={'cat': self.slug})

class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Nazwa'))
    slug = models.SlugField(max_length=30, unique=True, verbose_name=_('Nazwa w'
        ' URL'))
    category = models.ForeignKey('Category', verbose_name=_('Kategoria'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Autor'))
    content = models.TextField(null=True, blank=True, verbose_name=_('Treść'))
    datetime = models.DateTimeField(verbose_name=_('Data publikacji'))
    visible_only_for_staff = models.BooleanField(default=False,
        verbose_name=_('Widoczne tylko dla administracji'))

    class Meta:
        verbose_name = _('artykuł')
        verbose_name_plural = _('artykuły')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki:article', kwargs={'cat': self.category,
            'article': self.slug})
