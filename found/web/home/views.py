from django.views.generic import TemplateView

from web.projects.models import Project
from web.news.models import Entry


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_projects'] = Project.objects.all().order_by(
            '-created'
        )[:3]
        context['last_news'] = Entry.objects.all().order_by('-created')[:3]
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactsView(TemplateView):
    template_name = 'home/contacts.html'
