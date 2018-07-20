# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.4
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.weighted_variation import WeightedVariation  # noqa: F401,E501


class Rollout(object):
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
        'variations': 'list[WeightedVariation]'
    }

    attribute_map = {
        'variations': 'variations'
    }

    def __init__(self, variations=None):  # noqa: E501
        """Rollout - a model defined in Swagger"""  # noqa: E501

        self._variations = None
        self.discriminator = None

        if variations is not None:
            self.variations = variations

    @property
    def variations(self):
        """Gets the variations of this Rollout.  # noqa: E501


        :return: The variations of this Rollout.  # noqa: E501
        :rtype: list[WeightedVariation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this Rollout.


        :param variations: The variations of this Rollout.  # noqa: E501
        :type: list[WeightedVariation]
        """

        self._variations = variations

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Rollout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
