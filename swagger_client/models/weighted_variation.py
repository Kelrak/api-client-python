# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API

    OpenAPI spec version: 2.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WeightedVariation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'variation': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'variation': 'variation',
        'weight': 'weight'
    }

    def __init__(self, variation=None, weight=None):
        """
        WeightedVariation - a model defined in Swagger
        """

        self._variation = None
        self._weight = None

        if variation is not None:
          self.variation = variation
        if weight is not None:
          self.weight = weight

    @property
    def variation(self):
        """
        Gets the variation of this WeightedVariation.

        :return: The variation of this WeightedVariation.
        :rtype: int
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """
        Sets the variation of this WeightedVariation.

        :param variation: The variation of this WeightedVariation.
        :type: int
        """

        self._variation = variation

    @property
    def weight(self):
        """
        Gets the weight of this WeightedVariation.

        :return: The weight of this WeightedVariation.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this WeightedVariation.

        :param weight: The weight of this WeightedVariation.
        :type: int
        """

        self._weight = weight

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WeightedVariation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other