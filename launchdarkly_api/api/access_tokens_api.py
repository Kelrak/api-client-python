# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class AccessTokensApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_token(self, token_id, **kwargs):  # noqa: E501
        """Delete an access token by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_token_with_http_info(token_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_token_with_http_info(token_id, **kwargs)  # noqa: E501
            return data

    def delete_token_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Delete an access token by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params or
                params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `delete_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_id' in params:
            path_params['tokenId'] = params['token_id']  # noqa: E501

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
            '/tokens/{tokenId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token(self, token_id, **kwargs):  # noqa: E501
        """Get a single access token by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_with_http_info(token_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_with_http_info(token_id, **kwargs)  # noqa: E501
            return data

    def get_token_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Get a single access token by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params or
                params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `get_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_id' in params:
            path_params['tokenId'] = params['token_id']  # noqa: E501

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
            '/tokens/{tokenId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tokens(self, **kwargs):  # noqa: E501
        """Returns a list of tokens in the account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool show_all: If set to true, and the authentication access token has the \"Admin\" role, personal access tokens for all members will be retrieved.
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tokens_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tokens_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tokens_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of tokens in the account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool show_all: If set to true, and the authentication access token has the \"Admin\" role, personal access tokens for all members will be retrieved.
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['show_all']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tokens" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'show_all' in params:
            query_params.append(('showAll', params['show_all']))  # noqa: E501

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
            '/tokens', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_token(self, token_id, patch_delta, **kwargs):  # noqa: E501
        """Modify an access tokenby ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_token(token_id, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_token_with_http_info(token_id, patch_delta, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_token_with_http_info(token_id, patch_delta, **kwargs)  # noqa: E501
            return data

    def patch_token_with_http_info(self, token_id, patch_delta, **kwargs):  # noqa: E501
        """Modify an access tokenby ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_token_with_http_info(token_id, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_id', 'patch_delta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params or
                params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `patch_token`")  # noqa: E501
        # verify the required parameter 'patch_delta' is set
        if ('patch_delta' not in params or
                params['patch_delta'] is None):
            raise ValueError("Missing the required parameter `patch_delta` when calling `patch_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_id' in params:
            path_params['tokenId'] = params['token_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_delta' in params:
            body_params = params['patch_delta']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/tokens/{tokenId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_token(self, token_body, **kwargs):  # noqa: E501
        """Create a new token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_token(token_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenBody token_body: Create a new access token. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_token_with_http_info(token_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_token_with_http_info(token_body, **kwargs)  # noqa: E501
            return data

    def post_token_with_http_info(self, token_body, **kwargs):  # noqa: E501
        """Create a new token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_token_with_http_info(token_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenBody token_body: Create a new access token. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_body' is set
        if ('token_body' not in params or
                params['token_body'] is None):
            raise ValueError("Missing the required parameter `token_body` when calling `post_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'token_body' in params:
            body_params = params['token_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/tokens', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_token(self, token_id, **kwargs):  # noqa: E501
        """Reset an access token's secret key with an optional expiry time for the old key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_token(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :param int expiry: An expiration time for the old token key, expressed as a Unix epoch time in milliseconds. By default, the token will expire immediately.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_token_with_http_info(token_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_token_with_http_info(token_id, **kwargs)  # noqa: E501
            return data

    def reset_token_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Reset an access token's secret key with an optional expiry time for the old key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_token_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: The access token ID. (required)
        :param int expiry: An expiration time for the old token key, expressed as a Unix epoch time in milliseconds. By default, the token will expire immediately.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_id', 'expiry']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params or
                params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `reset_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_id' in params:
            path_params['tokenId'] = params['token_id']  # noqa: E501

        query_params = []
        if 'expiry' in params:
            query_params.append(('expiry', params['expiry']))  # noqa: E501

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
            '/tokens/{tokenId}/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
