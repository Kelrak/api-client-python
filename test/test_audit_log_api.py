# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API

    OpenAPI spec version: 2.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.audit_log_api import AuditLogApi


class TestAuditLogApi(unittest.TestCase):
    """ AuditLogApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.audit_log_api.AuditLogApi()

    def tearDown(self):
        pass

    def test_get_audit_log_entries(self):
        """
        Test case for get_audit_log_entries

        Fetch a list of all webhooks
        """
        pass

    def test_get_audit_log_entry(self):
        """
        Test case for get_audit_log_entry

        Get a webhook by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()