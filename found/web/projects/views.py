from django.views.generic.list import ListView


class ProjectsListView(ListView):
    template_name = 'projects/list.html'
    queryset  = set()
