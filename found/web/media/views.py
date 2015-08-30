from django.views.generic import TemplateView

from .models import PhotoGroup, VideoGroup


class MediaView(TemplateView):
    templates = 'media/view.html'

    def get_context_data(self, **kwargs):
        context = super(MediaView, self).get_context_data(**kwargs)
        context['video_groups'] = VideoGroup.objects.select_related('videos')
        context['photo_groups'] = PhotoGroup.objects.select_related('groups')
        return context
