from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Entry


class NewsListView(ListView):
    model = Entry
    template_name = 'news/list.html'


class NewsDetailView(DetailView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'news/detail.html'
