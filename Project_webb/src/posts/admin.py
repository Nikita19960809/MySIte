# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Post

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):

    list_display = 'title','author'
    search_fields = 'title','author'
    list_filter = 'is_archive',



