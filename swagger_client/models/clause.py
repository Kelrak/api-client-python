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


class Clause(object):
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
        'attribute': 'str',
        'op': 'str',
        'values': 'list[str]',
        'negate': 'bool'
    }

    attribute_map = {
        'attribute': 'attribute',
        'op': 'op',
        'values': 'values',
        'negate': 'negate'
    }

    def __init__(self, attribute=None, op=None, values=None, negate=None):
        """
        Clause - a model defined in Swagger
        """

        self._attribute = None
        self._op = None
        self._values = None
        self._negate = None

        if attribute is not None:
          self.attribute = attribute
        if op is not None:
          self.op = op
        if values is not None:
          self.values = values
        if negate is not None:
          self.negate = negate

    @property
    def attribute(self):
        """
        Gets the attribute of this Clause.

        :return: The attribute of this Clause.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """
        Sets the attribute of this Clause.

        :param attribute: The attribute of this Clause.
        :type: str
        """

        self._attribute = attribute

    @property
    def op(self):
        """
        Gets the op of this Clause.

        :return: The op of this Clause.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this Clause.

        :param op: The op of this Clause.
        :type: str
        """

        self._op = op

    @property
    def values(self):
        """
        Gets the values of this Clause.

        :return: The values of this Clause.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Clause.

        :param values: The values of this Clause.
        :type: list[str]
        """

        self._values = values

    @property
    def negate(self):
        """
        Gets the negate of this Clause.

        :return: The negate of this Clause.
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        """
        Sets the negate of this Clause.

        :param negate: The negate of this Clause.
        :type: bool
        """

        self._negate = negate

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
        if not isinstance(other, Clause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other