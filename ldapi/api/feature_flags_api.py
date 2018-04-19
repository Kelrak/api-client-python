# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ldapi.api_client import ApiClient


class FeatureFlagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_feature_flag(self, project_key, feature_flag_key, **kwargs):  # noqa: E501
        """Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_feature_flag(project_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_feature_flag_with_http_info(project_key, feature_flag_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_feature_flag_with_http_info(project_key, feature_flag_key, **kwargs)  # noqa: E501
            return data

    def delete_feature_flag_with_http_info(self, project_key, feature_flag_key, **kwargs):  # noqa: E501
        """Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_feature_flag_with_http_info(project_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'feature_flag_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `delete_feature_flag`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `delete_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flags/{projectKey}/{featureFlagKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flag(self, project_key, feature_flag_key, **kwargs):  # noqa: E501
        """Get a single feature flag by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag(project_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param str env: By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=production will restrict the returned configurations to just your production environment.
        :return: FeatureFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_feature_flag_with_http_info(project_key, feature_flag_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_flag_with_http_info(project_key, feature_flag_key, **kwargs)  # noqa: E501
            return data

    def get_feature_flag_with_http_info(self, project_key, feature_flag_key, **kwargs):  # noqa: E501
        """Get a single feature flag by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag_with_http_info(project_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param str env: By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=production will restrict the returned configurations to just your production environment.
        :return: FeatureFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'feature_flag_key', 'env']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_feature_flag`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `get_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

        query_params = []
        if 'env' in params:
            query_params.append(('env', params['env']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flags/{projectKey}/{featureFlagKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureFlag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flag_status(self, project_key, environment_key, feature_flag_key, **kwargs):  # noqa: E501
        """Get the status for a particular feature flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag_status(project_key, environment_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: FeatureFlagStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_feature_flag_status_with_http_info(project_key, environment_key, feature_flag_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_flag_status_with_http_info(project_key, environment_key, feature_flag_key, **kwargs)  # noqa: E501
            return data

    def get_feature_flag_status_with_http_info(self, project_key, environment_key, feature_flag_key, **kwargs):  # noqa: E501
        """Get the status for a particular feature flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag_status_with_http_info(project_key, environment_key, feature_flag_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: FeatureFlagStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'feature_flag_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flag_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_feature_flag_status`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_feature_flag_status`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `get_feature_flag_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureFlagStatus',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flag_statuses(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag_statuses(project_key, environment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :return: FeatureFlagStatuses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_feature_flag_statuses_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_flag_statuses_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
            return data

    def get_feature_flag_statuses_with_http_info(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flag_statuses_with_http_info(project_key, environment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :return: FeatureFlagStatuses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flag_statuses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_feature_flag_statuses`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_feature_flag_statuses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flag-statuses/{projectKey}/{environmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureFlagStatuses',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flags(self, project_key, **kwargs):  # noqa: E501
        """Get a list of all features in the given project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flags(project_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str env: By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=production will restrict the returned configurations to just your production environment.
        :param str tag: Filter by tag. A tag can be used to group flags across projects.
        :return: FeatureFlags
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_feature_flags_with_http_info(project_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_flags_with_http_info(project_key, **kwargs)  # noqa: E501
            return data

    def get_feature_flags_with_http_info(self, project_key, **kwargs):  # noqa: E501
        """Get a list of all features in the given project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_flags_with_http_info(project_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str env: By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=production will restrict the returned configurations to just your production environment.
        :param str tag: Filter by tag. A tag can be used to group flags across projects.
        :return: FeatureFlags
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'env', 'tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_feature_flags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501

        query_params = []
        if 'env' in params:
            query_params.append(('env', params['env']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flags/{projectKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureFlags',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_feature_flag(self, project_key, feature_flag_key, patch_comment, **kwargs):  # noqa: E501
        """Perform a partial update to a feature.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_feature_flag(project_key, feature_flag_key, patch_comment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param PatchComment patch_comment: Requires a JSON Patch representation of the desired changes to the project, and an optional comment. 'http://jsonpatch.com/' Feature flag patches also support JSON Merge Patch format. 'https://tools.ietf.org/html/rfc7386' The addition of comments is also supported. (required)
        :return: FeatureFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.patch_feature_flag_with_http_info(project_key, feature_flag_key, patch_comment, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_feature_flag_with_http_info(project_key, feature_flag_key, patch_comment, **kwargs)  # noqa: E501
            return data

    def patch_feature_flag_with_http_info(self, project_key, feature_flag_key, patch_comment, **kwargs):  # noqa: E501
        """Perform a partial update to a feature.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_feature_flag_with_http_info(project_key, feature_flag_key, patch_comment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param PatchComment patch_comment: Requires a JSON Patch representation of the desired changes to the project, and an optional comment. 'http://jsonpatch.com/' Feature flag patches also support JSON Merge Patch format. 'https://tools.ietf.org/html/rfc7386' The addition of comments is also supported. (required)
        :return: FeatureFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'feature_flag_key', 'patch_comment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `patch_feature_flag`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `patch_feature_flag`")  # noqa: E501
        # verify the required parameter 'patch_comment' is set
        if ('patch_comment' not in params or
                params['patch_comment'] is None):
            raise ValueError("Missing the required parameter `patch_comment` when calling `patch_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_comment' in params:
            body_params = params['patch_comment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flags/{projectKey}/{featureFlagKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureFlag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_feature_flag(self, project_key, feature_flag_body, **kwargs):  # noqa: E501
        """Creates a new feature flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_feature_flag(project_key, feature_flag_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param FeatureFlagBody feature_flag_body: Create a new feature flag. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_feature_flag_with_http_info(project_key, feature_flag_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_feature_flag_with_http_info(project_key, feature_flag_body, **kwargs)  # noqa: E501
            return data

    def post_feature_flag_with_http_info(self, project_key, feature_flag_body, **kwargs):  # noqa: E501
        """Creates a new feature flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_feature_flag_with_http_info(project_key, feature_flag_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param FeatureFlagBody feature_flag_body: Create a new feature flag. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'feature_flag_body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `post_feature_flag`")  # noqa: E501
        # verify the required parameter 'feature_flag_body' is set
        if ('feature_flag_body' not in params or
                params['feature_flag_body'] is None):
            raise ValueError("Missing the required parameter `feature_flag_body` when calling `post_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'feature_flag_body' in params:
            body_params = params['feature_flag_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/flags/{projectKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
