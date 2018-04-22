# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from application import settings
from django.db import models


class Tag(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name=u'Заголовок категории',
        default=""
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False, verbose_name=u'Категория в архиве')
    # post_tag = models.ForeignKey('posts.Post', related_name='categories', default="")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = 'title', 'id'
