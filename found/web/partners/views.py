from django.views.generic.list import ListView


class PartnersListView(ListView):
    template_name = 'partners/list.html'
    queryset = set()
