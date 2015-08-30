from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from web.projects.models import Project


class Entry(models.Model):
    main_image = models.ImageField(
        _('main image'),
        null=True,
        upload_to=settings.NEWS_UPLOAD_FOLDER
    )
    project = models.ForeignKey(Project, related_name='entries',
        verbose_name=_('project'), null=True)
    title = models.CharField(_('title'), max_length=255, unique=True)
    body = models.TextField(_('body'))
    is_recomended = models.BooleanField(_('is recomended'), default=False)
    is_anouns = models.BooleanField(_('is anouns'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name_plural = _('entries')

    def __str__(self):
        return '{}: {}'.format(_('news entry'), self.title)

    @property
    def slug(self):
        return '-'.join(self.title.split(' '))

    def main_admin_image(self):
        return '<img src="{}" width="100" height="100">'.format(
            self.main_image.url
        )
    main_admin_image.allow_tags = True
