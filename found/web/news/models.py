from django.db import models
from django.utils.translation import ugettext as _


class Entry(models.Model):
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    attachments = models.FileField(_('attachments'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name_plural = _('entries')

    def __str__(self):
        return '{0} {1}'.format(_('News Entry model'), self.title)

    @property
    def slug(self):
        return '-'.join(self.title.split(''))
