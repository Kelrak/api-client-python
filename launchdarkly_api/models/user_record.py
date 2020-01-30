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

from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.user import User  # noqa: F401,E501


class UserRecord(object):
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
        'last_ping': 'str',
        'environment_id': 'str',
        'owner_id': 'Id',
        'user': 'User',
        'avatar': 'str'
    }

    attribute_map = {
        'last_ping': 'lastPing',
        'environment_id': 'environmentId',
        'owner_id': 'ownerId',
        'user': 'user',
        'avatar': 'avatar'
    }

    def __init__(self, last_ping=None, environment_id=None, owner_id=None, user=None, avatar=None):  # noqa: E501
        """UserRecord - a model defined in Swagger"""  # noqa: E501

        self._last_ping = None
        self._environment_id = None
        self._owner_id = None
        self._user = None
        self._avatar = None
        self.discriminator = None

        if last_ping is not None:
            self.last_ping = last_ping
        if environment_id is not None:
            self.environment_id = environment_id
        if owner_id is not None:
            self.owner_id = owner_id
        if user is not None:
            self.user = user
        if avatar is not None:
            self.avatar = avatar

    @property
    def last_ping(self):
        """Gets the last_ping of this UserRecord.  # noqa: E501


        :return: The last_ping of this UserRecord.  # noqa: E501
        :rtype: str
        """
        return self._last_ping

    @last_ping.setter
    def last_ping(self, last_ping):
        """Sets the last_ping of this UserRecord.


        :param last_ping: The last_ping of this UserRecord.  # noqa: E501
        :type: str
        """

        self._last_ping = last_ping

    @property
    def environment_id(self):
        """Gets the environment_id of this UserRecord.  # noqa: E501


        :return: The environment_id of this UserRecord.  # noqa: E501
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this UserRecord.


        :param environment_id: The environment_id of this UserRecord.  # noqa: E501
        :type: str
        """

        self._environment_id = environment_id

    @property
    def owner_id(self):
        """Gets the owner_id of this UserRecord.  # noqa: E501


        :return: The owner_id of this UserRecord.  # noqa: E501
        :rtype: Id
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this UserRecord.


        :param owner_id: The owner_id of this UserRecord.  # noqa: E501
        :type: Id
        """

        self._owner_id = owner_id

    @property
    def user(self):
        """Gets the user of this UserRecord.  # noqa: E501


        :return: The user of this UserRecord.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserRecord.


        :param user: The user of this UserRecord.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def avatar(self):
        """Gets the avatar of this UserRecord.  # noqa: E501


        :return: The avatar of this UserRecord.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this UserRecord.


        :param avatar: The avatar of this UserRecord.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

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
        if issubclass(UserRecord, dict):
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
        if not isinstance(other, UserRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
