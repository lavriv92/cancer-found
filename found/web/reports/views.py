from django.views.generic.list import ListView

from .models import Report


class ReportsListView(ListView):
    model = Report
    template_name = 'reports/list.html'
