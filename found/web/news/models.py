from django.db import models
from django.utils.translation import ugettext as _

from web.projects.models import Project


class Entry(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('project'), null=True)
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name_plural = _('entries')

    def __str__(self):
        return '{}: {}'.format(_('news entry'), self.title)

    @property
    def slug(self):
        return '-'.join(self.title.split(' '))
