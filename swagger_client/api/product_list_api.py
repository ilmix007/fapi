# coding: utf-8

"""
    База кроссов автозапчастей FAPI. Описание доступа через API

    База кроссов автозапчастей FAPI. Описание доступа через API  # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: development.iisis@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ProductListApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def image_list_get(self, mfi, n, **kwargs):  # noqa: E501
        """Получение картинки  # noqa: E501

        Используйте одельный сервер для работы с картинками: https://static.fapi.iisis.ru/fapi/v2/imageList  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_list_get(mfi, n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int mfi: Индекс производителя (required)
        :param str n: Номер детали (required)
        :param int width: Ширина картинки
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_list_get_with_http_info(mfi, n, **kwargs)  # noqa: E501
        else:
            (data) = self.image_list_get_with_http_info(mfi, n, **kwargs)  # noqa: E501
            return data

    def image_list_get_with_http_info(self, mfi, n, **kwargs):  # noqa: E501
        """Получение картинки  # noqa: E501

        Используйте одельный сервер для работы с картинками: https://static.fapi.iisis.ru/fapi/v2/imageList  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_list_get_with_http_info(mfi, n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int mfi: Индекс производителя (required)
        :param str n: Номер детали (required)
        :param int width: Ширина картинки
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mfi', 'n', 'width']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mfi' is set
        if ('mfi' not in params or
                params['mfi'] is None):
            raise ValueError("Missing the required parameter `mfi` when calling `image_list_get`")  # noqa: E501
        # verify the required parameter 'n' is set
        if ('n' not in params or
                params['n'] is None):
            raise ValueError("Missing the required parameter `n` when calling `image_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mfi' in params:
            query_params.append(('mfi', params['mfi']))  # noqa: E501
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imageList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_applicability_list_get(self, mfi, n, **kwargs):  # noqa: E501
        """Применяемость детали к автомобилям  # noqa: E501

        Применяемость детали к автомобилям(модель,модификация)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_applicability_list_get(mfi, n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int mfi: Индекс бренда (required)
        :param str n: Артикул(номер) детали (required)
        :return: CarListV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_applicability_list_get_with_http_info(mfi, n, **kwargs)  # noqa: E501
        else:
            (data) = self.product_applicability_list_get_with_http_info(mfi, n, **kwargs)  # noqa: E501
            return data

    def product_applicability_list_get_with_http_info(self, mfi, n, **kwargs):  # noqa: E501
        """Применяемость детали к автомобилям  # noqa: E501

        Применяемость детали к автомобилям(модель,модификация)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_applicability_list_get_with_http_info(mfi, n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int mfi: Индекс бренда (required)
        :param str n: Артикул(номер) детали (required)
        :return: CarListV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mfi', 'n']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_applicability_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mfi' is set
        if ('mfi' not in params or
                params['mfi'] is None):
            raise ValueError("Missing the required parameter `mfi` when calling `product_applicability_list_get`")  # noqa: E501
        # verify the required parameter 'n' is set
        if ('n' not in params or
                params['n'] is None):
            raise ValueError("Missing the required parameter `n` when calling `product_applicability_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mfi' in params:
            query_params.append(('mfi', params['mfi']))  # noqa: E501
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/productApplicabilityList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CarListV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_list_get(self, n, **kwargs):  # noqa: E501
        """Детали  # noqa: E501

        Детали  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_list_get(n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали или начальная часть артикула (required)
        :param bool comparison: Если установлен, то параметр n будет являться шаблоном поиска артикула
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_list_get_with_http_info(n, **kwargs)  # noqa: E501
        else:
            (data) = self.product_list_get_with_http_info(n, **kwargs)  # noqa: E501
            return data

    def product_list_get_with_http_info(self, n, **kwargs):  # noqa: E501
        """Детали  # noqa: E501

        Детали  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_list_get_with_http_info(n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали или начальная часть артикула (required)
        :param bool comparison: Если установлен, то параметр n будет являться шаблоном поиска артикула
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['n', 'comparison']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'n' is set
        if ('n' not in params or
                params['n'] is None):
            raise ValueError("Missing the required parameter `n` when calling `product_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501
        if 'comparison' in params:
            query_params.append(('comparison', params['comparison']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/productList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_number_list_get(self, n, **kwargs):  # noqa: E501
        """Получить список номеров  # noqa: E501

        Получить список номеров  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_number_list_get(n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали или начальная часть артикула (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_number_list_get_with_http_info(n, **kwargs)  # noqa: E501
        else:
            (data) = self.product_number_list_get_with_http_info(n, **kwargs)  # noqa: E501
            return data

    def product_number_list_get_with_http_info(self, n, **kwargs):  # noqa: E501
        """Получить список номеров  # noqa: E501

        Получить список номеров  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_number_list_get_with_http_info(n, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали или начальная часть артикула (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['n']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_number_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'n' is set
        if ('n' not in params or
                params['n'] is None):
            raise ValueError("Missing the required parameter `n` when calling `product_number_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/productNumberList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_parameter_list_get(self, n, mfi, **kwargs):  # noqa: E501
        """Дополнительная информации о детали  # noqa: E501

        Получить список номеров  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_parameter_list_get(n, mfi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали (required)
        :param int mfi: Индекс бренда (required)
        :return: list[ParameterListRow]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_parameter_list_get_with_http_info(n, mfi, **kwargs)  # noqa: E501
        else:
            (data) = self.product_parameter_list_get_with_http_info(n, mfi, **kwargs)  # noqa: E501
            return data

    def product_parameter_list_get_with_http_info(self, n, mfi, **kwargs):  # noqa: E501
        """Дополнительная информации о детали  # noqa: E501

        Получить список номеров  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_parameter_list_get_with_http_info(n, mfi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str n: Артикул(номер) детали (required)
        :param int mfi: Индекс бренда (required)
        :return: list[ParameterListRow]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['n', 'mfi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_parameter_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'n' is set
        if ('n' not in params or
                params['n'] is None):
            raise ValueError("Missing the required parameter `n` when calling `product_parameter_list_get`")  # noqa: E501
        # verify the required parameter 'mfi' is set
        if ('mfi' not in params or
                params['mfi'] is None):
            raise ValueError("Missing the required parameter `mfi` when calling `product_parameter_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501
        if 'mfi' in params:
            query_params.append(('mfi', params['mfi']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/productParameterList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ParameterListRow]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)