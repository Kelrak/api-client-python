# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.4.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Defaults(object):
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
        'on_variation': 'int',
        'off_variation': 'int'
    }

    attribute_map = {
        'on_variation': 'onVariation',
        'off_variation': 'offVariation'
    }

    def __init__(self, on_variation=None, off_variation=None):  # noqa: E501
        """Defaults - a model defined in Swagger"""  # noqa: E501

        self._on_variation = None
        self._off_variation = None
        self.discriminator = None

        self.on_variation = on_variation
        self.off_variation = off_variation

    @property
    def on_variation(self):
        """Gets the on_variation of this Defaults.  # noqa: E501

        The index of the variation to be served when a flag's targeting is on (default variation).  # noqa: E501

        :return: The on_variation of this Defaults.  # noqa: E501
        :rtype: int
        """
        return self._on_variation

    @on_variation.setter
    def on_variation(self, on_variation):
        """Sets the on_variation of this Defaults.

        The index of the variation to be served when a flag's targeting is on (default variation).  # noqa: E501

        :param on_variation: The on_variation of this Defaults.  # noqa: E501
        :type: int
        """
        if on_variation is None:
            raise ValueError("Invalid value for `on_variation`, must not be `None`")  # noqa: E501

        self._on_variation = on_variation

    @property
    def off_variation(self):
        """Gets the off_variation of this Defaults.  # noqa: E501

        The index of the variation to be served when a flag is off.  # noqa: E501

        :return: The off_variation of this Defaults.  # noqa: E501
        :rtype: int
        """
        return self._off_variation

    @off_variation.setter
    def off_variation(self, off_variation):
        """Sets the off_variation of this Defaults.

        The index of the variation to be served when a flag is off.  # noqa: E501

        :param off_variation: The off_variation of this Defaults.  # noqa: E501
        :type: int
        """
        if off_variation is None:
            raise ValueError("Invalid value for `off_variation`, must not be `None`")  # noqa: E501

        self._off_variation = off_variation

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
        if issubclass(Defaults, dict):
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
        if not isinstance(other, Defaults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
