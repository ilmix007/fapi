# coding: utf-8

"""
    База кроссов автозапчастей FAPI. Описание доступа через API

    База кроссов автозапчастей FAPI. Описание доступа через API  # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: development.iisis@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.analog_list import AnalogList  # noqa: F401,E501
from swagger_client.models.manufacturer_list import ManufacturerList  # noqa: F401,E501
from swagger_client.models.product_list import ProductList  # noqa: F401,E501


class AnalogListV2(object):
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
        'manufacturer_list': 'ManufacturerList',
        'product_list': 'ProductList',
        'analog_list': 'AnalogList'
    }

    attribute_map = {
        'manufacturer_list': 'manufacturerList',
        'product_list': 'productList',
        'analog_list': 'analogList'
    }

    def __init__(self, manufacturer_list=None, product_list=None, analog_list=None):  # noqa: E501
        """AnalogListV2 - a model defined in Swagger"""  # noqa: E501

        self._manufacturer_list = None
        self._product_list = None
        self._analog_list = None
        self.discriminator = None

        self.manufacturer_list = manufacturer_list
        self.product_list = product_list
        self.analog_list = analog_list

    @property
    def manufacturer_list(self):
        """Gets the manufacturer_list of this AnalogListV2.  # noqa: E501


        :return: The manufacturer_list of this AnalogListV2.  # noqa: E501
        :rtype: ManufacturerList
        """
        return self._manufacturer_list

    @manufacturer_list.setter
    def manufacturer_list(self, manufacturer_list):
        """Sets the manufacturer_list of this AnalogListV2.


        :param manufacturer_list: The manufacturer_list of this AnalogListV2.  # noqa: E501
        :type: ManufacturerList
        """
        if manufacturer_list is None:
            raise ValueError("Invalid value for `manufacturer_list`, must not be `None`")  # noqa: E501

        self._manufacturer_list = manufacturer_list

    @property
    def product_list(self):
        """Gets the product_list of this AnalogListV2.  # noqa: E501


        :return: The product_list of this AnalogListV2.  # noqa: E501
        :rtype: ProductList
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list):
        """Sets the product_list of this AnalogListV2.


        :param product_list: The product_list of this AnalogListV2.  # noqa: E501
        :type: ProductList
        """
        if product_list is None:
            raise ValueError("Invalid value for `product_list`, must not be `None`")  # noqa: E501

        self._product_list = product_list

    @property
    def analog_list(self):
        """Gets the analog_list of this AnalogListV2.  # noqa: E501


        :return: The analog_list of this AnalogListV2.  # noqa: E501
        :rtype: AnalogList
        """
        return self._analog_list

    @analog_list.setter
    def analog_list(self, analog_list):
        """Sets the analog_list of this AnalogListV2.


        :param analog_list: The analog_list of this AnalogListV2.  # noqa: E501
        :type: AnalogList
        """
        if analog_list is None:
            raise ValueError("Invalid value for `analog_list`, must not be `None`")  # noqa: E501

        self._analog_list = analog_list

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
        if issubclass(AnalogListV2, dict):
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
        if not isinstance(other, AnalogListV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
