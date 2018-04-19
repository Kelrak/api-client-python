# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ldapi.models.id import Id  # noqa: F401,E501
from ldapi.models.links import Links  # noqa: F401,E501


class Webhook(object):
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
        'url': 'str',
        'secret': 'str',
        'on': 'bool',
        'name': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'url': 'url',
        'secret': 'secret',
        'on': 'on',
        'name': 'name',
        'tags': 'tags'
    }

    def __init__(self, links=None, id=None, url=None, secret=None, on=None, name=None, tags=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._url = None
        self._secret = None
        self._on = None
        self._name = None
        self._tags = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if secret is not None:
            self.secret = secret
        if on is not None:
            self.on = on
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags

    @property
    def links(self):
        """Gets the links of this Webhook.  # noqa: E501


        :return: The links of this Webhook.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Webhook.


        :param links: The links of this Webhook.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501


        :return: The id of this Webhook.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.


        :param id: The id of this Webhook.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501

        The URL of the remote webhook.  # noqa: E501

        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.

        The URL of the remote webhook.  # noqa: E501

        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this Webhook.  # noqa: E501

        If defined, the webhooks post request will include a X-LD-Signature header whose value will contain an HMAC SHA256 hex digest of the webhook payload, using the secret as the key.  # noqa: E501

        :return: The secret of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this Webhook.

        If defined, the webhooks post request will include a X-LD-Signature header whose value will contain an HMAC SHA256 hex digest of the webhook payload, using the secret as the key.  # noqa: E501

        :param secret: The secret of this Webhook.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def on(self):
        """Gets the on of this Webhook.  # noqa: E501

        Whether this webhook is enabled or not.  # noqa: E501

        :return: The on of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """Sets the on of this Webhook.

        Whether this webhook is enabled or not.  # noqa: E501

        :param on: The on of this Webhook.  # noqa: E501
        :type: bool
        """

        self._on = on

    @property
    def name(self):
        """Gets the name of this Webhook.  # noqa: E501

        The name of the webhook.  # noqa: E501

        :return: The name of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Webhook.

        The name of the webhook.  # noqa: E501

        :param name: The name of this Webhook.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this Webhook.  # noqa: E501

        Tags assigned to this webhook.  # noqa: E501

        :return: The tags of this Webhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Webhook.

        Tags assigned to this webhook.  # noqa: E501

        :param tags: The tags of this Webhook.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
