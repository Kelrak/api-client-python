# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.26
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.feature_flags_api import FeatureFlagsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestFeatureFlagsApi(unittest.TestCase):
    """FeatureFlagsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.feature_flags_api.FeatureFlagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_feature_flag(self):
        """Test case for copy_feature_flag

        Copies the feature flag configuration from one environment to the same feature flag in another environment.  # noqa: E501
        """
        pass

    def test_delete_feature_flag(self):
        """Test case for delete_feature_flag

        Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.  # noqa: E501
        """
        pass

    def test_get_feature_flag(self):
        """Test case for get_feature_flag

        Get a single feature flag by key.  # noqa: E501
        """
        pass

    def test_get_feature_flag_status(self):
        """Test case for get_feature_flag_status

        Get the status for a particular feature flag.  # noqa: E501
        """
        pass

    def test_get_feature_flag_status_across_environments(self):
        """Test case for get_feature_flag_status_across_environments

        Get the status for a particular feature flag across environments  # noqa: E501
        """
        pass

    def test_get_feature_flag_statuses(self):
        """Test case for get_feature_flag_statuses

        Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.  # noqa: E501
        """
        pass

    def test_get_feature_flags(self):
        """Test case for get_feature_flags

        Get a list of all features in the given project.  # noqa: E501
        """
        pass

    def test_patch_feature_flag(self):
        """Test case for patch_feature_flag

        Perform a partial update to a feature.  # noqa: E501
        """
        pass

    def test_post_feature_flag(self):
        """Test case for post_feature_flag

        Creates a new feature flag.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
