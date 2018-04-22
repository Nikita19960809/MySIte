# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tag

class TagList(ListView):
    template_name = "tags/tag_list.html"
    model = Tag


def tag_detail(request, pk=None):

    category = get_object_or_404(Tag, id=pk)

    context = {
        'category': Tag.objects.get(id=pk),
        'posts': category.posts.all().filter(is_archive=False)
    }
    return render(request, 'tags/tag_detail.html', context)
