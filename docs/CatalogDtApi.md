# swagger_client.CatalogDtApi

All URIs are relative to *https://fapi.iisis.ru/fapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_list_dt_manufacturer_list_get**](CatalogDtApi.md#catalog_list_dt_manufacturer_list_get) | **GET** /catalogList/dt/manufacturerList | Получение списка производителей
[**catalog_list_dt_model_list_get**](CatalogDtApi.md#catalog_list_dt_model_list_get) | **GET** /catalogList/dt/modelList | Список моделей
[**catalog_list_dt_modification_list_get**](CatalogDtApi.md#catalog_list_dt_modification_list_get) | **GET** /catalogList/dt/modificationList | Список модификаций модели


# **catalog_list_dt_manufacturer_list_get**
> ManufacturerList catalog_list_dt_manufacturer_list_get()

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
api_instance = swagger_client.CatalogDtApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка производителей
    api_response = api_instance.catalog_list_dt_manufacturer_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogDtApi->catalog_list_dt_manufacturer_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManufacturerList**](ManufacturerList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_list_dt_model_list_get**
> ModelList catalog_list_dt_model_list_get(mfi)

Список моделей

Получение списка моделей по выбранной марке автомобиля

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
api_instance = swagger_client.CatalogDtApi(swagger_client.ApiClient(configuration))
mfi = 106 # int | Идентификатор производителя (default to 106)

try:
    # Список моделей
    api_response = api_instance.catalog_list_dt_model_list_get(mfi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogDtApi->catalog_list_dt_model_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfi** | **int**| Идентификатор производителя | [default to 106]

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_list_dt_modification_list_get**
> ModificationList catalog_list_dt_modification_list_get(mi)

Список модификаций модели

Получение списка модификаций по выбранной модели

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
api_instance = swagger_client.CatalogDtApi(swagger_client.ApiClient(configuration))
mi = 6363 # int | Идентификатор(dbi) модели (default to 6363)

try:
    # Список модификаций модели
    api_response = api_instance.catalog_list_dt_modification_list_get(mi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogDtApi->catalog_list_dt_modification_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mi** | **int**| Идентификатор(dbi) модели | [default to 6363]

### Return type

[**ModificationList**](ModificationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

