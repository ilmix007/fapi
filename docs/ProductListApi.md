# swagger_client.ProductListApi

All URIs are relative to *https://fapi.iisis.ru/fapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_list_get**](ProductListApi.md#image_list_get) | **GET** /imageList | Получение картинки
[**product_applicability_list_get**](ProductListApi.md#product_applicability_list_get) | **GET** /productApplicabilityList | Применяемость детали к автомобилям
[**product_list_get**](ProductListApi.md#product_list_get) | **GET** /productList | Детали
[**product_number_list_get**](ProductListApi.md#product_number_list_get) | **GET** /productNumberList | Получить список номеров
[**product_parameter_list_get**](ProductListApi.md#product_parameter_list_get) | **GET** /productParameterList | Дополнительная информации о детали


# **image_list_get**
> image_list_get(mfi, n, width=width)

Получение картинки

Используйте одельный сервер для работы с картинками: https://static.fapi.iisis.ru/fapi/v2/imageList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductListApi()
mfi = 13007 # int | Индекс производителя (default to 13007)
n = '10100' # str | Номер детали (default to 10100)
width = 200 # int | Ширина картинки (optional) (default to 200)

try:
    # Получение картинки
    api_instance.image_list_get(mfi, n, width=width)
except ApiException as e:
    print("Exception when calling ProductListApi->image_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfi** | **int**| Индекс производителя | [default to 13007]
 **n** | **str**| Номер детали | [default to 10100]
 **width** | **int**| Ширина картинки | [optional] [default to 200]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_applicability_list_get**
> CarListV2 product_applicability_list_get(mfi, n)

Применяемость детали к автомобилям

Применяемость детали к автомобилям(модель,модификация)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['ui'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ui'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProductListApi(swagger_client.ApiClient(configuration))
mfi = 12738 # int | Индекс бренда (default to 12738)
n = 'AG+251' # str | Артикул(номер) детали (default to AG+251)

try:
    # Применяемость детали к автомобилям
    api_response = api_instance.product_applicability_list_get(mfi, n)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductListApi->product_applicability_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfi** | **int**| Индекс бренда | [default to 12738]
 **n** | **str**| Артикул(номер) детали | [default to AG+251]

### Return type

[**CarListV2**](CarListV2.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_get**
> product_list_get(n, comparison=comparison)

Детали

Детали

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['ui'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ui'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProductListApi(swagger_client.ApiClient(configuration))
n = 'A00742' # str | Артикул(номер) детали или начальная часть артикула (default to A00742)
comparison = true # bool | Если установлен, то параметр n будет являться шаблоном поиска артикула (optional)

try:
    # Детали
    api_instance.product_list_get(n, comparison=comparison)
except ApiException as e:
    print("Exception when calling ProductListApi->product_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| Артикул(номер) детали или начальная часть артикула | [default to A00742]
 **comparison** | **bool**| Если установлен, то параметр n будет являться шаблоном поиска артикула | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_number_list_get**
> list[str] product_number_list_get(n)

Получить список номеров

Получить список номеров

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['ui'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ui'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProductListApi(swagger_client.ApiClient(configuration))
n = 'A00742' # str | Артикул(номер) детали или начальная часть артикула (default to A00742)

try:
    # Получить список номеров
    api_response = api_instance.product_number_list_get(n)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductListApi->product_number_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| Артикул(номер) детали или начальная часть артикула | [default to A00742]

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_parameter_list_get**
> list[ParameterListRow] product_parameter_list_get(n, mfi)

Дополнительная информации о детали

Получить список номеров

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['ui'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ui'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProductListApi(swagger_client.ApiClient(configuration))
n = '10100' # str | Артикул(номер) детали (default to 10100)
mfi = 13007 # int | Индекс бренда (default to 13007)

try:
    # Дополнительная информации о детали
    api_response = api_instance.product_parameter_list_get(n, mfi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductListApi->product_parameter_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| Артикул(номер) детали | [default to 10100]
 **mfi** | **int**| Индекс бренда | [default to 13007]

### Return type

[**list[ParameterListRow]**](ParameterListRow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

