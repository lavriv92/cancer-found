from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Partner(models.Model):
    logo = models.ImageField(_('logo'),
        upload_to=settings.PARTNERS_UPLOAD_FOLDER)
    url = models.URLField(_('url'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('partner')
