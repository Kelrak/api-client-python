# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.26
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.links import Links  # noqa: F401,E501


class FeatureFlagStatus(object):
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
        'name': 'str',
        'last_requested': 'str',
        'default': 'object',
        'links': 'Links'
    }

    attribute_map = {
        'name': 'name',
        'last_requested': 'lastRequested',
        'default': 'default',
        'links': '_links'
    }

    def __init__(self, name=None, last_requested=None, default=None, links=None):  # noqa: E501
        """FeatureFlagStatus - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._last_requested = None
        self._default = None
        self._links = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if last_requested is not None:
            self.last_requested = last_requested
        if default is not None:
            self.default = default
        if links is not None:
            self.links = links

    @property
    def name(self):
        """Gets the name of this FeatureFlagStatus.  # noqa: E501

        | Name     | Description | | --------:| ----------- | | new      | the feature flag was created within the last 7 days, and has not been requested yet | | active   | the feature flag was requested by your servers or clients within the last 7 days | | inactive | the feature flag was created more than 7 days ago, and hasn't been requested by your servers or clients within the past 7 days | | launched | one variation of the feature flag has been rolled out to all your users for at least 7 days |   # noqa: E501

        :return: The name of this FeatureFlagStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureFlagStatus.

        | Name     | Description | | --------:| ----------- | | new      | the feature flag was created within the last 7 days, and has not been requested yet | | active   | the feature flag was requested by your servers or clients within the last 7 days | | inactive | the feature flag was created more than 7 days ago, and hasn't been requested by your servers or clients within the past 7 days | | launched | one variation of the feature flag has been rolled out to all your users for at least 7 days |   # noqa: E501

        :param name: The name of this FeatureFlagStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["new", "active", "inactive", "launched"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def last_requested(self):
        """Gets the last_requested of this FeatureFlagStatus.  # noqa: E501


        :return: The last_requested of this FeatureFlagStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_requested

    @last_requested.setter
    def last_requested(self, last_requested):
        """Sets the last_requested of this FeatureFlagStatus.


        :param last_requested: The last_requested of this FeatureFlagStatus.  # noqa: E501
        :type: str
        """

        self._last_requested = last_requested

    @property
    def default(self):
        """Gets the default of this FeatureFlagStatus.  # noqa: E501


        :return: The default of this FeatureFlagStatus.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this FeatureFlagStatus.


        :param default: The default of this FeatureFlagStatus.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def links(self):
        """Gets the links of this FeatureFlagStatus.  # noqa: E501


        :return: The links of this FeatureFlagStatus.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureFlagStatus.


        :param links: The links of this FeatureFlagStatus.  # noqa: E501
        :type: Links
        """

        self._links = links

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
        if issubclass(FeatureFlagStatus, dict):
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
        if not isinstance(other, FeatureFlagStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
