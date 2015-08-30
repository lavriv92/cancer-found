from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class MemeberGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class Memeber(models.Model):
    photo = models.ImageField(_('photo'),
        upload_to=settings.MEMBERS_UPLOAD_FOLDER)
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    position = models.CharField(_('position'), max_length=255)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)


    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Document(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    doc_file = models.FileField(_('doc_file'),
        upload_to=settings.FILES_UPLOAD_FOLDER)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')


class VolonteerTask(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
