# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
import datetime

from django.conf import settings
from django.db import models



class Question(models.Model):

    author_question = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор вопроса',default="")
    description = models.TextField(verbose_name=u'Текст вопроса',default="")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    category_quest = models.ForeignKey('tags.Tag', related_name='questions', verbose_name=u'Категория вопроса', default="")

    def __unicode__(self):
        return self.description


class Answer(models.Model):

    author_answer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор ответа',default="")
    description = models.TextField(verbose_name=u'Текст ответа', default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    question_answer = models.ForeignKey('questions.Question', related_name='answers', verbose_name=u'Ответ на вопрос', default="")

    def __unicode__(self):
        return self.description