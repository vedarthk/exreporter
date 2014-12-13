# -*- coding: utf-8 -*-

"""
exporter.contrib.django_middlewares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements Django middlewares for different stores.
Requires following Django settings to be present:
- EXREPORTER_GIHUB_USER
- EXREPORTER_GIHUB_REPO
- EXREPORTER_GIHUB_AUTH_TOKEN
- EXREPORTER_GIHUB_LABELS

:copyright: (c) 2014 by Vedarth Kulkarni.
:license: MIT, see LICENSE for more details.

"""

from django.conf import settings
from exreporter.credentials import GithubCredentials
from exreporter import exreporter


class ExreporterGithubMiddleware(object):
    """Exreporter middleware for Django framework.
    """

    def process_exception(self, request, exception):
        """Report exceptions from requests via Exreporter.
        """
        credentials = GithubCredentials(
            user=settings.EXREPORTER_GIHUB_USER,
            repo=settings.EXREPORTER_GIHUB_REPO,
            auth_token=settings.EXREPORTER_GIHUB_AUTH_TOKEN)

        exreporter.report_github_issue(
            credentials=credentials, labels=settings.EXREPORTER_GIHUB_LABELS)
