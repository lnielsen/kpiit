# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# KPIit is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""MetricInstances for Zenodo."""

from ..metrics.records import RecordsMetric
from ..metricsinst.records import RecordsMetricInst
from ..providers import JSONURLProvider


class ZenodoRecordsMetricInst(RecordsMetricInst):
    """Metric instance for # of records from Zenodo."""

    URL = 'https://zenodo.org/api/records/?all_versions'

    def __init__(self, provider=JSONURLProvider(RecordsMetric(), URL)):
        """Number of records metric for Zenodo initialization."""
        super().__init__(provider)
