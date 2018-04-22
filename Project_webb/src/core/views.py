# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from posts.models import Post
from questions.models import Question
from tags.models import Tag

def index(request):
    posts = Post.objects.all()[:5]
    questions = Question.objects.all()[:5]
    tags = Tag.objects.all()

    context = {
        'posts':posts,
        'questions':questions,
        'tags':tags,

    }
    return render(request,'core/index.html',context)

