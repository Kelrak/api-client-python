# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.12
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.environments_api import EnvironmentsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestEnvironmentsApi(unittest.TestCase):
    """EnvironmentsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.environments_api.EnvironmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_environment(self):
        """Test case for delete_environment

        Delete an environment in a specific project.  # noqa: E501
        """
        pass

    def test_get_environment(self):
        """Test case for get_environment

        Get an environment given a project and key.  # noqa: E501
        """
        pass

    def test_patch_environment(self):
        """Test case for patch_environment

        Modify an environment by ID.  # noqa: E501
        """
        pass

    def test_post_environment(self):
        """Test case for post_environment

        Create a new environment in a specified project with a given name, key, and swatch color.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
