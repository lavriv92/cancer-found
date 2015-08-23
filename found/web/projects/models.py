from django.db import models
from django.utils.translation import ugettext as _


class Project(models.Model):

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __str__(self):
        return '{} {}'.format(_('project'), self.name)
