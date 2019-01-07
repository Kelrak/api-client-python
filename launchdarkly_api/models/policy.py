# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.12
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.actions import Actions  # noqa: F401,E501
from launchdarkly_api.models.resources import Resources  # noqa: F401,E501


class Policy(object):
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
        'resources': 'Resources',
        'actions': 'Actions',
        'effect': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'actions': 'actions',
        'effect': 'effect'
    }

    def __init__(self, resources=None, actions=None, effect=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501

        self._resources = None
        self._actions = None
        self._effect = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if actions is not None:
            self.actions = actions
        if effect is not None:
            self.effect = effect

    @property
    def resources(self):
        """Gets the resources of this Policy.  # noqa: E501


        :return: The resources of this Policy.  # noqa: E501
        :rtype: Resources
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Policy.


        :param resources: The resources of this Policy.  # noqa: E501
        :type: Resources
        """

        self._resources = resources

    @property
    def actions(self):
        """Gets the actions of this Policy.  # noqa: E501


        :return: The actions of this Policy.  # noqa: E501
        :rtype: Actions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Policy.


        :param actions: The actions of this Policy.  # noqa: E501
        :type: Actions
        """

        self._actions = actions

    @property
    def effect(self):
        """Gets the effect of this Policy.  # noqa: E501

        Effect of the policy - allow or deny.  # noqa: E501

        :return: The effect of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Policy.

        Effect of the policy - allow or deny.  # noqa: E501

        :param effect: The effect of this Policy.  # noqa: E501
        :type: str
        """

        self._effect = effect

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
