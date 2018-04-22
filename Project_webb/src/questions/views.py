# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Question

class QuestionList(ListView):
    template_name = "questions/question_list.html"
    model = Question

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'questions/question_detail.html', {'question': question})