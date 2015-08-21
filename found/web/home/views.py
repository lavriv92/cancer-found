from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'
