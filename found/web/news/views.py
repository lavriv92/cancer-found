from django.shortcuts import render
from django.views.generic.list import ListView


class NewsListView(ListView):
    template_name = 'news/list.html'
    queryset = set()
