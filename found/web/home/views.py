from django.views.generic import TemplateView

from web.projects.models import Project
from web.news.models import Entry
from .models import MemeberGroup, Document


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_projects'] = Project.objects.all().order_by(
            '-created'
        )[:3]
        context['last_news'] = Entry.objects.all().order_by('-created')[:3]
        context['recomended_news'] = Entry.objects.filter(
            is_recomended=True
        ).order_by('-created')[:3]
        context['anounsed_news'] = Entry.objects.filter(
            is_anouns=True
        ).order_by('-created')[:3]
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['member_groups'] = MemeberGroup.objects.select_related('members').all()
        context['documents'] = Document.objects.all().order_by('-created')
        return context


class ContactsView(TemplateView):
    template_name = 'home/contacts.html'
