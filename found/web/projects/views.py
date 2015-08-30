from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Project


class ProjectsListView(ListView):
    template_name = 'projects/list.html'
    model = Project


class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project
