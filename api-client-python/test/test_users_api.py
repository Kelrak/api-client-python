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
from launchdarkly_api.api.users_api import UsersApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user by ID.  # noqa: E501
        """
        pass

    def test_get_search_users(self):
        """Test case for get_search_users

        Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a user by key.  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List all users in the environment. Includes the total count of users. In each page, there will be up to 'limit' users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()