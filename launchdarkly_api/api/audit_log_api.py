# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.23
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class AuditLogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_audit_log_entries(self, **kwargs):  # noqa: E501
        """Get a list of all audit log entries. The query parameters allow you to restrict the returned results by date ranges, resource specifiers, or a full-text search query.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_entries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int before: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have before this timestamp.
        :param int after: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have occured after this timestamp.
        :param str q: Text to search for. You can search for the full or partial name of the resource involved or fullpartial email address of the member who made the change.
        :param float limit: A limit on the number of audit log entries to be returned, between 1 and 20.
        :param str spec: A resource specifier, allowing you to filter audit log listings by resource.
        :return: AuditLogEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_log_entries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_log_entries_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_audit_log_entries_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of all audit log entries. The query parameters allow you to restrict the returned results by date ranges, resource specifiers, or a full-text search query.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_entries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int before: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have before this timestamp.
        :param int after: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have occured after this timestamp.
        :param str q: Text to search for. You can search for the full or partial name of the resource involved or fullpartial email address of the member who made the change.
        :param float limit: A limit on the number of audit log entries to be returned, between 1 and 20.
        :param str spec: A resource specifier, allowing you to filter audit log listings by resource.
        :return: AuditLogEntries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['before', 'after', 'q', 'limit', 'spec']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_log_entries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'spec' in params:
            query_params.append(('spec', params['spec']))  # noqa: E501

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
            '/auditlog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditLogEntries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_log_entry(self, resource_id, **kwargs):  # noqa: E501
        """Use this endpoint to fetch a single audit log entry by its resouce ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_entry(resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource_id: The resource ID. (required)
        :return: AuditLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_log_entry_with_http_info(resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_log_entry_with_http_info(resource_id, **kwargs)  # noqa: E501
            return data

    def get_audit_log_entry_with_http_info(self, resource_id, **kwargs):  # noqa: E501
        """Use this endpoint to fetch a single audit log entry by its resouce ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_entry_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str resource_id: The resource ID. (required)
        :return: AuditLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_log_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_audit_log_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

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
            '/auditlog/{resourceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditLogEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
