# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# KPIit is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Publisher instances."""

from .cern import CERNMonitPublisher
from .json import JSONFilePublisher


#: Zenodo DOI publisher
zenodo_doi = CERNMonitPublisher.create_doi('10.5281')

#: CDS videos DOI publisher
cds_videos_doi = CERNMonitPublisher.create_doi('10.17181')

#: COD DOI publisher
cod_doi = CERNMonitPublisher.create_doi('10.7483')


#: Zenodo repo publisher
zenodo_repo = CERNMonitPublisher.create_repo('zenodo', 'qa')

#: CDS videos repo publisher
cds_videos_repo = CERNMonitPublisher.create_repo('cds_videos', 'qa')

#: COD repo publisher
cod_repo = CERNMonitPublisher.create_repo('cod', 'qa')
