# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.dispatch.dispatcher import receiver
from model_utils.choices import Choices
from djspikeval.models import Result

__all__ = ["ResultDefault"]


class ResultDefault(Result):
    """default result entity"""

    # meta
    class Meta:
        app_label = "djspikeval_default"
        verbose_name = "Result(Default)"
        verbose_name_plural = "Results(Default)"

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

    # interface
    def __unicode__(self):
        return unicode("{} kind={}".format(super(ResultDefault, self).__unicode__(), self.kind))


@receiver(models.signals.pre_delete, sender=ResultDefault)
def image_file_delete(sender, instance, **kwargs):
    instance.file.delete()


if __name__ == "__main__":
    pass
