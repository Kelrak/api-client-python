# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.23
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DestinationAmazonKinesis(object):
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
        'region': 'str',
        'role_arn': 'str',
        'stream_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'role_arn': 'roleArn',
        'stream_name': 'streamName'
    }

    def __init__(self, region=None, role_arn=None, stream_name=None):  # noqa: E501
        """DestinationAmazonKinesis - a model defined in Swagger"""  # noqa: E501

        self._region = None
        self._role_arn = None
        self._stream_name = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if role_arn is not None:
            self.role_arn = role_arn
        if stream_name is not None:
            self.stream_name = stream_name

    @property
    def region(self):
        """Gets the region of this DestinationAmazonKinesis.  # noqa: E501


        :return: The region of this DestinationAmazonKinesis.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DestinationAmazonKinesis.


        :param region: The region of this DestinationAmazonKinesis.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def role_arn(self):
        """Gets the role_arn of this DestinationAmazonKinesis.  # noqa: E501


        :return: The role_arn of this DestinationAmazonKinesis.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this DestinationAmazonKinesis.


        :param role_arn: The role_arn of this DestinationAmazonKinesis.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def stream_name(self):
        """Gets the stream_name of this DestinationAmazonKinesis.  # noqa: E501


        :return: The stream_name of this DestinationAmazonKinesis.  # noqa: E501
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this DestinationAmazonKinesis.


        :param stream_name: The stream_name of this DestinationAmazonKinesis.  # noqa: E501
        :type: str
        """

        self._stream_name = stream_name

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
        if issubclass(DestinationAmazonKinesis, dict):
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
        if not isinstance(other, DestinationAmazonKinesis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
