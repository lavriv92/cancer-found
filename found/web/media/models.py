from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class PhotoGroup(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.CharField(_('description'), max_length=300)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return '{}: {}'.format(_('Photo group'), self.title)


class Photo(models.Model):
    group = models.ForeignKey(PhotoGroup, verbose_name=_('group'))
    image = models.ImageField(_('image'),
        upload_to=settings.MEDIAPHOTOS_UPLOAD_FOLDER)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('photo')

    @property
    def src(self):
        return self.image.url

    def __str__(self):
        return '{}: {}'.format(_('photo'), self.src)

class VideoGroup(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('video group')
        verbose_name_plural = _('video groups')


class Video(models.Model):
    group = models.ForeignKey(VideoGroup, verbose_name=_('video group'))
    video = models.FileField(_('video'),
        upload_to=settings.VIDEOS_UPLOAD_FOLDER)
    created = models.DateTimeField(_('created'), auto_now=True)
    updated = models.DateTimeField(_('updated'), auto_now_add=True)

    class Meta:
        verbose_name = _('video')
