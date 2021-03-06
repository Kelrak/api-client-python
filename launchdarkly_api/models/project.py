# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.client_side_availability import ClientSideAvailability  # noqa: F401,E501
from launchdarkly_api.models.environment import Environment  # noqa: F401,E501
from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501


class Project(object):
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
        'key': 'str',
        'name': 'str',
        'include_in_snippet_by_default': 'bool',
        'environments': 'list[Environment]',
        'tags': 'list[str]',
        'default_client_side_availability': 'ClientSideAvailability'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'key': 'key',
        'name': 'name',
        'include_in_snippet_by_default': 'includeInSnippetByDefault',
        'environments': 'environments',
        'tags': 'tags',
        'default_client_side_availability': 'defaultClientSideAvailability'
    }

    def __init__(self, links=None, id=None, key=None, name=None, include_in_snippet_by_default=None, environments=None, tags=None, default_client_side_availability=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._key = None
        self._name = None
        self._include_in_snippet_by_default = None
        self._environments = None
        self._tags = None
        self._default_client_side_availability = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if include_in_snippet_by_default is not None:
            self.include_in_snippet_by_default = include_in_snippet_by_default
        if environments is not None:
            self.environments = environments
        if tags is not None:
            self.tags = tags
        if default_client_side_availability is not None:
            self.default_client_side_availability = default_client_side_availability

    @property
    def links(self):
        """Gets the links of this Project.  # noqa: E501


        :return: The links of this Project.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Project.


        :param links: The links of this Project.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this Project.  # noqa: E501


        :return: The key of this Project.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Project.


        :param key: The key of this Project.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def include_in_snippet_by_default(self):
        """Gets the include_in_snippet_by_default of this Project.  # noqa: E501


        :return: The include_in_snippet_by_default of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_snippet_by_default

    @include_in_snippet_by_default.setter
    def include_in_snippet_by_default(self, include_in_snippet_by_default):
        """Sets the include_in_snippet_by_default of this Project.


        :param include_in_snippet_by_default: The include_in_snippet_by_default of this Project.  # noqa: E501
        :type: bool
        """

        self._include_in_snippet_by_default = include_in_snippet_by_default

    @property
    def environments(self):
        """Gets the environments of this Project.  # noqa: E501


        :return: The environments of this Project.  # noqa: E501
        :rtype: list[Environment]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this Project.


        :param environments: The environments of this Project.  # noqa: E501
        :type: list[Environment]
        """

        self._environments = environments

    @property
    def tags(self):
        """Gets the tags of this Project.  # noqa: E501

        An array of tags for this project.  # noqa: E501

        :return: The tags of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Project.

        An array of tags for this project.  # noqa: E501

        :param tags: The tags of this Project.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def default_client_side_availability(self):
        """Gets the default_client_side_availability of this Project.  # noqa: E501


        :return: The default_client_side_availability of this Project.  # noqa: E501
        :rtype: ClientSideAvailability
        """
        return self._default_client_side_availability

    @default_client_side_availability.setter
    def default_client_side_availability(self, default_client_side_availability):
        """Sets the default_client_side_availability of this Project.


        :param default_client_side_availability: The default_client_side_availability of this Project.  # noqa: E501
        :type: ClientSideAvailability
        """

        self._default_client_side_availability = default_client_side_availability

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
