# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.29
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.user_settings_api import UserSettingsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestUserSettingsApi(unittest.TestCase):
    """UserSettingsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.user_settings_api.UserSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_flag_setting(self):
        """Test case for get_user_flag_setting

        Fetch a single flag setting for a user by key.  # noqa: E501
        """
        pass

    def test_get_user_flag_settings(self):
        """Test case for get_user_flag_settings

        Fetch a single flag setting for a user by key.  # noqa: E501
        """
        pass

    def test_put_flag_setting(self):
        """Test case for put_flag_setting

        Specifically enable or disable a feature flag for a user based on their key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()