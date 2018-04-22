# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class Post(models.Model):

    author_post = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор поста', default="")
    title = models.CharField(max_length=200, verbose_name=u'Имя поста', default="None")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    description = models.TextField(default="", verbose_name=u'Описание поста')
    category_post = models.ManyToManyField('tags.Tag', blank=True, related_name='posts',
                                        verbose_name=u'Категории')
    is_archive = models.BooleanField(default=False, verbose_name=u'Пост в архиве')

    def __unicode__(self):
        return self.title

