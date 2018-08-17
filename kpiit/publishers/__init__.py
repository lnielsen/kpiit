# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# KPIit is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Publisher instances."""

from kpiit.publishers.cern import CERNMonitPublisher


#: DOI publisher
doi = CERNMonitPublisher.create_doi

#: Repo publisher
repo = CERNMonitPublisher.create_repo
