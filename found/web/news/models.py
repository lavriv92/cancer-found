from django.db import models
from django.utils.translation import ugettex_lazy as _


class Entry(models.Model):
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    slug = models.SlugField(_('slug'), max_length=255)
    attachments = models.FileField()
