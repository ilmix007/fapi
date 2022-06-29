# swagger_client.ManufacturerListApi

All URIs are relative to *https://fapi.iisis.ru/fapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manufacturer_list_get**](ManufacturerListApi.md#manufacturer_list_get) | **GET** /manufacturerList | Получение списка производителей


# **manufacturer_list_get**
> ManufacturerList manufacturer_list_get(mfd=mfd)

Получение списка производителей

Метод используют для выпадающего списка для выбора производителя

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
api_instance = swagger_client.ManufacturerListApi(swagger_client.ApiClient(configuration))
mfd = 'merc' # str | Часть наименования производителя. Если не указан, будет выведен весь список (optional) (default to merc)

try:
    # Получение списка производителей
    api_response = api_instance.manufacturer_list_get(mfd=mfd)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManufacturerListApi->manufacturer_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfd** | **str**| Часть наименования производителя. Если не указан, будет выведен весь список | [optional] [default to merc]

### Return type

[**ManufacturerList**](ManufacturerList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

