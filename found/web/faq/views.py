from django.views.generic import TemplateView


class FaqView(TemplateView):
    template_name = 'faq/view.html'
