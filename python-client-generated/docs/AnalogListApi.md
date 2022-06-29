# swagger_client.AnalogListApi

All URIs are relative to *https://fapi.iisis.ru/fapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analog_list_get**](AnalogListApi.md#analog_list_get) | **GET** /analogList | Получить кроссы
[**analog_list_post**](AnalogListApi.md#analog_list_post) | **POST** /analogList | Добавить кроссы в общую базу


# **analog_list_get**
> AnalogListV2 analog_list_get(n, mfi=mfi, r=r, o=o)

Получить кроссы

Получить объект кроссы

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
api_instance = swagger_client.AnalogListApi(swagger_client.ApiClient(configuration))
n = 'A0074207920' # str | Артикул(номер) детали (default to A0074207920)
mfi = 56 # int | Индекс бренда (optional)
r = 0 # int | Фильтр по рейтингу кросса (optional) (default to 0)
o = 'NOT_USE' # str | Дополнительный фильтр: NOT_USE - не использовать дополнительный фильтр ONLY_OWN - только собственные(верные или битые), ar не учитывать CORRECT_AR - только собственные(верные) с участием фильтра по рейтингу. Если аналог не имеет указанного при фильтрации рейтинга, но указан как верный, он попадает в выдачу  (optional) (default to NOT_USE)

try:
    # Получить кроссы
    api_response = api_instance.analog_list_get(n, mfi=mfi, r=r, o=o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalogListApi->analog_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| Артикул(номер) детали | [default to A0074207920]
 **mfi** | **int**| Индекс бренда | [optional] 
 **r** | **int**| Фильтр по рейтингу кросса | [optional] [default to 0]
 **o** | **str**| Дополнительный фильтр: NOT_USE - не использовать дополнительный фильтр ONLY_OWN - только собственные(верные или битые), ar не учитывать CORRECT_AR - только собственные(верные) с участием фильтра по рейтингу. Если аналог не имеет указанного при фильтрации рейтинга, но указан как верный, он попадает в выдачу  | [optional] [default to NOT_USE]

### Return type

[**AnalogListV2**](AnalogListV2.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analog_list_post**
> analog_list_post(ui, inventory_item=inventory_item)

Добавить кроссы в общую базу

Добавление кроссов в общую базу. Добавить можно сразу несколько кроссов. При добавлении одного или нескольких кроссов автоматически происходит голосование за кросс. Через данный метод можно также голосовать за битый кросс(За это отвечает свойство _int - 0(кросс верный), 1(кросс битый))

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
api_instance = swagger_client.AnalogListApi(swagger_client.ApiClient(configuration))
ui = '6c4a4367-c7b0-4263-ae20-0038273ab2e7' # str | Идентификатор пользователя (default to 6c4a4367-c7b0-4263-ae20-0038273ab2e7)
inventory_item = swagger_client.AnalogListPost() # AnalogListPost | Inventory item to add (optional)

try:
    # Добавить кроссы в общую базу
    api_instance.analog_list_post(ui, inventory_item=inventory_item)
except ApiException as e:
    print("Exception when calling AnalogListApi->analog_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ui** | **str**| Идентификатор пользователя | [default to 6c4a4367-c7b0-4263-ae20-0038273ab2e7]
 **inventory_item** | [**AnalogListPost**](AnalogListPost.md)| Inventory item to add | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

