# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.24
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DestinationGooglePubSub(object):
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
        'project': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'project': 'project',
        'topic': 'topic'
    }

    def __init__(self, project=None, topic=None):  # noqa: E501
        """DestinationGooglePubSub - a model defined in Swagger"""  # noqa: E501

        self._project = None
        self._topic = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if topic is not None:
            self.topic = topic

    @property
    def project(self):
        """Gets the project of this DestinationGooglePubSub.  # noqa: E501


        :return: The project of this DestinationGooglePubSub.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DestinationGooglePubSub.


        :param project: The project of this DestinationGooglePubSub.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def topic(self):
        """Gets the topic of this DestinationGooglePubSub.  # noqa: E501


        :return: The topic of this DestinationGooglePubSub.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this DestinationGooglePubSub.


        :param topic: The topic of this DestinationGooglePubSub.  # noqa: E501
        :type: str
        """

        self._topic = topic

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
        if issubclass(DestinationGooglePubSub, dict):
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
        if not isinstance(other, DestinationGooglePubSub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other