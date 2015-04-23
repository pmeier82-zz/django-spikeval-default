# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from StringIO import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import get_object_or_404
from spikeval.module import ModDefault, ModuleExecutionError
from .models.result import ResultDefault

__author__ = "pmeier82"
__all__ = ["ModuleDefault"]


class ModuleDefault(ModDefault):
    """spikeval module for default visuals"""

    # RESULT_TYPES
    # 10 'wf_single'    MRPlot, # waveforms by units
    # 20 'wf_all'       MRPlot, # waveforms all spikes
    # 30 'clus12'       MRPlot, # cluster PC1/2
    # 40 'clus34'       MRPlot, # cluster PC3/4
    # 50 'clus_proj'    MRPlot, # cluster projection
    # 60 'spiketrain'   MRPlot] # spike train set

    def save(self, mod, ana):
        """save django result entities"""

        # check for results
        if self._stage != 3:
            raise ModuleExecutionError("save initiated when module was not finalised!")

        # per result saving:
        for i, res in enumerate(self.result):
            # result
            kind = (i + 1) * 10
            res_entity, _ = ResultDefault.objects.get_or_create(analysis=ana, module=mod, kind=kind)

            # data
            img_data = StringIO()
            res.value.save(img_data, format="PNG")

            # filename
            try:
                kindname = ResultDefault.KIND[kind]
            except:
                kindname = "unknown{}".format(i)
            filename = "ana{:04d}_{}.png".format(ana.id, kindname)

            # file
            if res_entity.file is not None:
                res_entity.file.delete()
            res_entity.file = InMemoryUploadedFile(
                file=img_data,
                field_name=None,
                name=filename,
                content_type="image/png",
                size=img_data.len,
                charset=None)
            res_entity.save()


if __name__ == "__main__":
    pass
