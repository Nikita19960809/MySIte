# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Comment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    description = models.TextField(default="",verbose_name=u'Описание коммента')
    #author_comment= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments',verbose_name=u'Автор комментария',default="")
    post_comment = models.ForeignKey('posts.Post',verbose_name='Пост к комменту',default="")
    question_comment = models.ForeignKey('questions.Question',verbose_name='Вопрос к комменту',related_name='comments_quest',default="")
    #answer = models.ForeignKey('questions.Answer')

    def __str__(self):
        return self.description

