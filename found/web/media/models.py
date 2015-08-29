from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Galery(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.CharField(_('description'), max_length=300)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    photos = models.ManyToManyField('Photo', _('photos'))

    class Meta:
        verbose_name = _('galery')
        verbose_name_plural = _('galeries')

    def __str__(self):
        return '{}: {}'.format(_('Galery'), self.title)


class Photo(models.Model):
    image = models.ImageField(_('image'), upload_to="photos")
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('photo')

    @property
    def src(self):
        return self.image.url

    def __str__(self):
        return '{}: {}'.format(_('photo'), self.src)
