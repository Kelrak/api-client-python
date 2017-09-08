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


class Webhook(object):
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
        'links': 'Links',
        'id': 'str',
        'url': 'str',
        'secret': 'str',
        'on': 'bool',
        'tags': 'list[str]'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'url': 'url',
        'secret': 'secret',
        'on': 'on',
        'tags': 'tags'
    }

    def __init__(self, links=None, id=None, url=None, secret=None, on=None, tags=None):
        """
        Webhook - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._url = None
        self._secret = None
        self._on = None
        self._tags = None

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
        if tags is not None:
          self.tags = tags

    @property
    def links(self):
        """
        Gets the links of this Webhook.

        :return: The links of this Webhook.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Webhook.

        :param links: The links of this Webhook.
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Webhook.

        :return: The id of this Webhook.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Webhook.

        :param id: The id of this Webhook.
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this Webhook.

        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Webhook.

        :param url: The url of this Webhook.
        :type: str
        """

        self._url = url

    @property
    def secret(self):
        """
        Gets the secret of this Webhook.

        :return: The secret of this Webhook.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this Webhook.

        :param secret: The secret of this Webhook.
        :type: str
        """

        self._secret = secret

    @property
    def on(self):
        """
        Gets the on of this Webhook.

        :return: The on of this Webhook.
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """
        Sets the on of this Webhook.

        :param on: The on of this Webhook.
        :type: bool
        """

        self._on = on

    @property
    def tags(self):
        """
        Gets the tags of this Webhook.

        :return: The tags of this Webhook.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Webhook.

        :param tags: The tags of this Webhook.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
