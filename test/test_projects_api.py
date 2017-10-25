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
from swagger_client.apis.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ ProjectsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.projects_api.ProjectsApi()

    def tearDown(self):
        pass

    def test_delete_project(self):
        """
        Test case for delete_project

        Delete a project by ID
        """
        pass

    def test_get_project(self):
        """
        Test case for get_project

        Fetch a single project by key.
        """
        pass

    def test_get_projects(self):
        """
        Test case for get_projects

        Returns a list of all projects in the account.
        """
        pass

    def test_patch_project(self):
        """
        Test case for patch_project

        Modify a project by ID
        """
        pass

    def test_post_project(self):
        """
        Test case for post_project

        Create a project
        """
        pass


if __name__ == '__main__':
    unittest.main()
