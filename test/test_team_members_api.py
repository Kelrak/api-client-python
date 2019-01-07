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
from launchdarkly_api.api.team_members_api import TeamMembersApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestTeamMembersApi(unittest.TestCase):
    """TeamMembersApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.team_members_api.TeamMembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_member(self):
        """Test case for delete_member

        Delete a team member by ID.  # noqa: E501
        """
        pass

    def test_get_member(self):
        """Test case for get_member

        Get a single team member by ID.  # noqa: E501
        """
        pass

    def test_get_members(self):
        """Test case for get_members

        Returns a list of all members in the account.  # noqa: E501
        """
        pass

    def test_patch_member(self):
        """Test case for patch_member

        Modify a team member by ID.  # noqa: E501
        """
        pass

    def test_post_members(self):
        """Test case for post_members

        Invite new members.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
