# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from model_utils.choices import Choices
from djspikeval.models import Result

__all__ = ["ResultDefault"]


class ResultDefault(Result):
    """default result image"""

    # meta
    class Meta:
        app_label = "djspikeval_default"

    # order
    KIND = Choices(
        (00, "unknown"),
        (10, "wf_single"),
        (20, "wf_all"),
        (30, "clus12"),
        (40, "clus34"),
        (50, "clus_proj"),
        (60, "spiketrain"),
    )

    # fields
    file = models.ImageField(upload_to="results_default")
    kind = models.IntegerField(choices=KIND, default=00)


if __name__ == "__main__":
    pass
