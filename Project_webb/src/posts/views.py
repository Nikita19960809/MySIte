# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,get_object_or_404

from django.views.generic import DetailView, ListView
from .models import Post

class PostList(ListView):
    template_name = "posts/post_list.html"
    model = Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': Post.objects.get(id=pk),
        'categories': post.category_post.all().filter(is_archive=False)
    }

    return render(request, 'posts/post_detail.html', context)

