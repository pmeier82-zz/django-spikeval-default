# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .models import ResultDefault

__author__ = "pmeier82"


class ResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(ResultDefault, ResultAdmin)

if __name__ == "__main__":
    pass
