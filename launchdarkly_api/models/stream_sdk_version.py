# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.3.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.stream_by_sdk_links import StreamBySDKLinks  # noqa: F401,E501
from launchdarkly_api.models.stream_sdk_version_data import StreamSDKVersionData  # noqa: F401,E501


class StreamSDKVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'StreamBySDKLinks',
        'sdk_versions': 'list[StreamSDKVersionData]'
    }

    attribute_map = {
        'links': '_links',
        'sdk_versions': 'sdkVersions'
    }

    def __init__(self, links=None, sdk_versions=None):  # noqa: E501
        """StreamSDKVersion - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._sdk_versions = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if sdk_versions is not None:
            self.sdk_versions = sdk_versions

    @property
    def links(self):
        """Gets the links of this StreamSDKVersion.  # noqa: E501


        :return: The links of this StreamSDKVersion.  # noqa: E501
        :rtype: StreamBySDKLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StreamSDKVersion.


        :param links: The links of this StreamSDKVersion.  # noqa: E501
        :type: StreamBySDKLinks
        """

        self._links = links

    @property
    def sdk_versions(self):
        """Gets the sdk_versions of this StreamSDKVersion.  # noqa: E501


        :return: The sdk_versions of this StreamSDKVersion.  # noqa: E501
        :rtype: list[StreamSDKVersionData]
        """
        return self._sdk_versions

    @sdk_versions.setter
    def sdk_versions(self, sdk_versions):
        """Sets the sdk_versions of this StreamSDKVersion.


        :param sdk_versions: The sdk_versions of this StreamSDKVersion.  # noqa: E501
        :type: list[StreamSDKVersionData]
        """

        self._sdk_versions = sdk_versions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StreamSDKVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamSDKVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
