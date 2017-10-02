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


class FeatureFlagConfig(object):
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
        'on': 'bool',
        'archived': 'bool',
        'salt': 'str',
        'sel': 'str',
        'last_modified': 'int',
        'version': 'int',
        'targets': 'list[Target]',
        'rules': 'list[Rule]',
        'fallthrough': 'FeatureFlagConfigFallthrough'
    }

    attribute_map = {
        'on': 'on',
        'archived': 'archived',
        'salt': 'salt',
        'sel': 'sel',
        'last_modified': 'lastModified',
        'version': 'version',
        'targets': 'targets',
        'rules': 'rules',
        'fallthrough': 'fallthrough'
    }

    def __init__(self, on=None, archived=None, salt=None, sel=None, last_modified=None, version=None, targets=None, rules=None, fallthrough=None):
        """
        FeatureFlagConfig - a model defined in Swagger
        """

        self._on = None
        self._archived = None
        self._salt = None
        self._sel = None
        self._last_modified = None
        self._version = None
        self._targets = None
        self._rules = None
        self._fallthrough = None

        if on is not None:
          self.on = on
        if archived is not None:
          self.archived = archived
        if salt is not None:
          self.salt = salt
        if sel is not None:
          self.sel = sel
        if last_modified is not None:
          self.last_modified = last_modified
        if version is not None:
          self.version = version
        if targets is not None:
          self.targets = targets
        if rules is not None:
          self.rules = rules
        if fallthrough is not None:
          self.fallthrough = fallthrough

    @property
    def on(self):
        """
        Gets the on of this FeatureFlagConfig.

        :return: The on of this FeatureFlagConfig.
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """
        Sets the on of this FeatureFlagConfig.

        :param on: The on of this FeatureFlagConfig.
        :type: bool
        """

        self._on = on

    @property
    def archived(self):
        """
        Gets the archived of this FeatureFlagConfig.

        :return: The archived of this FeatureFlagConfig.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this FeatureFlagConfig.

        :param archived: The archived of this FeatureFlagConfig.
        :type: bool
        """

        self._archived = archived

    @property
    def salt(self):
        """
        Gets the salt of this FeatureFlagConfig.

        :return: The salt of this FeatureFlagConfig.
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """
        Sets the salt of this FeatureFlagConfig.

        :param salt: The salt of this FeatureFlagConfig.
        :type: str
        """

        self._salt = salt

    @property
    def sel(self):
        """
        Gets the sel of this FeatureFlagConfig.

        :return: The sel of this FeatureFlagConfig.
        :rtype: str
        """
        return self._sel

    @sel.setter
    def sel(self, sel):
        """
        Sets the sel of this FeatureFlagConfig.

        :param sel: The sel of this FeatureFlagConfig.
        :type: str
        """

        self._sel = sel

    @property
    def last_modified(self):
        """
        Gets the last_modified of this FeatureFlagConfig.

        :return: The last_modified of this FeatureFlagConfig.
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this FeatureFlagConfig.

        :param last_modified: The last_modified of this FeatureFlagConfig.
        :type: int
        """

        self._last_modified = last_modified

    @property
    def version(self):
        """
        Gets the version of this FeatureFlagConfig.

        :return: The version of this FeatureFlagConfig.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FeatureFlagConfig.

        :param version: The version of this FeatureFlagConfig.
        :type: int
        """

        self._version = version

    @property
    def targets(self):
        """
        Gets the targets of this FeatureFlagConfig.

        :return: The targets of this FeatureFlagConfig.
        :rtype: list[Target]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this FeatureFlagConfig.

        :param targets: The targets of this FeatureFlagConfig.
        :type: list[Target]
        """

        self._targets = targets

    @property
    def rules(self):
        """
        Gets the rules of this FeatureFlagConfig.

        :return: The rules of this FeatureFlagConfig.
        :rtype: list[Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this FeatureFlagConfig.

        :param rules: The rules of this FeatureFlagConfig.
        :type: list[Rule]
        """

        self._rules = rules

    @property
    def fallthrough(self):
        """
        Gets the fallthrough of this FeatureFlagConfig.

        :return: The fallthrough of this FeatureFlagConfig.
        :rtype: FeatureFlagConfigFallthrough
        """
        return self._fallthrough

    @fallthrough.setter
    def fallthrough(self, fallthrough):
        """
        Sets the fallthrough of this FeatureFlagConfig.

        :param fallthrough: The fallthrough of this FeatureFlagConfig.
        :type: FeatureFlagConfigFallthrough
        """

        self._fallthrough = fallthrough

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
        if not isinstance(other, FeatureFlagConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other