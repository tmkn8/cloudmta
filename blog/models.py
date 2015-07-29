from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext as _

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Tytuł'))
    slug = models.SlugField(max_length=30, unique=True, verbose_name=_('nazwa '
        'w URL'))
    content = models.TextField(null=True, blank=True, verbose_name=_('treść'),
        help_text=_('Markdown'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('autor'))
    publish_date = models.DateTimeField(verbose_name=_('data opublikowania'))
    hidden = models.BooleanField(default=True, verbose_name=_('ukryty'),
        help_text=_('widoczny tylko dla członków ekipy z linkiem do postu'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posty')

    def __str__(self):
        return self.title

    def get_absolute_url(request):
        return reverse('blog:article', kwargs={'slug': self.slug})

    def format_content(self):
        import markdown
        return markdown.markdown(self.content)
