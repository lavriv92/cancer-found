from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _



class Report(models.Model):
    title = models.CharField(_('title'), max_length=255)
    report_file = models.FileField(_('file'), upload_to=settings.REPORTS_UPLOAD_FOLDER)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('report')
        verbose_name_plural = _('reports')
