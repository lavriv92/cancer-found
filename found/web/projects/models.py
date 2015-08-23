from django.db import models
from django.utils.translation import ugettext as _


class Project(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __str__(self):
        return '{}: {}'.format(_('project'), self.title)
