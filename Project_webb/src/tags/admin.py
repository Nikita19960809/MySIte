# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Tag

admin.site.register(Tag)


class CategoryAdmin(admin.ModelAdmin):

    list_display = 'name'
    search_fields = 'name'
    list_filter = 'is_archive',
