# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__author__ = "pmeier82"


class DjSpikevalDefaultAppConfig(AppConfig):
    label = "djspikeval_default"
    name = "djspikeval_default"
    verbose_name = _("Django Spikeval - Default")

    def ready(self):
        # import all parts of the application that need to be exposed
        pass


if __name__ == "__main__":
    pass
