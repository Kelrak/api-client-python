# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.6
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.role import Role  # noqa: F401,E501


class Member(object):
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
        'links': 'Links',
        'id': 'Id',
        'role': 'Role',
        'email': 'str',
        'pending_invite': 'bool',
        'is_beta': 'bool',
        'custom_roles': 'list[Id]'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'role': 'role',
        'email': 'email',
        'pending_invite': '_pendingInvite',
        'is_beta': 'isBeta',
        'custom_roles': 'customRoles'
    }

    def __init__(self, links=None, id=None, role=None, email=None, pending_invite=None, is_beta=None, custom_roles=None):  # noqa: E501
        """Member - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._role = None
        self._email = None
        self._pending_invite = None
        self._is_beta = None
        self._custom_roles = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if email is not None:
            self.email = email
        if pending_invite is not None:
            self.pending_invite = pending_invite
        if is_beta is not None:
            self.is_beta = is_beta
        if custom_roles is not None:
            self.custom_roles = custom_roles

    @property
    def links(self):
        """Gets the links of this Member.  # noqa: E501


        :return: The links of this Member.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Member.


        :param links: The links of this Member.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Member.  # noqa: E501


        :return: The id of this Member.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.


        :param id: The id of this Member.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this Member.  # noqa: E501


        :return: The role of this Member.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Member.


        :param role: The role of this Member.  # noqa: E501
        :type: Role
        """

        self._role = role

    @property
    def email(self):
        """Gets the email of this Member.  # noqa: E501


        :return: The email of this Member.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Member.


        :param email: The email of this Member.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def pending_invite(self):
        """Gets the pending_invite of this Member.  # noqa: E501


        :return: The pending_invite of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._pending_invite

    @pending_invite.setter
    def pending_invite(self, pending_invite):
        """Sets the pending_invite of this Member.


        :param pending_invite: The pending_invite of this Member.  # noqa: E501
        :type: bool
        """

        self._pending_invite = pending_invite

    @property
    def is_beta(self):
        """Gets the is_beta of this Member.  # noqa: E501


        :return: The is_beta of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._is_beta

    @is_beta.setter
    def is_beta(self, is_beta):
        """Sets the is_beta of this Member.


        :param is_beta: The is_beta of this Member.  # noqa: E501
        :type: bool
        """

        self._is_beta = is_beta

    @property
    def custom_roles(self):
        """Gets the custom_roles of this Member.  # noqa: E501


        :return: The custom_roles of this Member.  # noqa: E501
        :rtype: list[Id]
        """
        return self._custom_roles

    @custom_roles.setter
    def custom_roles(self, custom_roles):
        """Sets the custom_roles of this Member.


        :param custom_roles: The custom_roles of this Member.  # noqa: E501
        :type: list[Id]
        """

        self._custom_roles = custom_roles

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other