from django.views.generic.list import ListView

from .models import Project

class ProjectsListView(ListView):
    template_name = 'projects/list.html'
    model = Project
