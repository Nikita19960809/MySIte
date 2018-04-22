# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Comment

class CommentList(ListView):

    template_name = "comments/comment_list.html"
    model = Comment