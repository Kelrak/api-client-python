# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.31
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Target(object):
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
        'values': 'list[str]',
        'variation': 'int'
    }

    attribute_map = {
        'values': 'values',
        'variation': 'variation'
    }

    def __init__(self, values=None, variation=None):  # noqa: E501
        """Target - a model defined in Swagger"""  # noqa: E501

        self._values = None
        self._variation = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if variation is not None:
            self.variation = variation

    @property
    def values(self):
        """Gets the values of this Target.  # noqa: E501


        :return: The values of this Target.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Target.


        :param values: The values of this Target.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    @property
    def variation(self):
        """Gets the variation of this Target.  # noqa: E501


        :return: The variation of this Target.  # noqa: E501
        :rtype: int
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this Target.


        :param variation: The variation of this Target.  # noqa: E501
        :type: int
        """

        self._variation = variation

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
        if issubclass(Target, dict):
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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
