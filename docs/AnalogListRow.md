# AnalogListRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i** | **int** | Index / Индекс | 
**pri** | **int** | Не используется | [optional] 
**si** | **int** | Не используется | [optional] 
**di** | **int** | Не используется | [optional] 
**_int** | **int** | Маркер(битый | верный), если вы голосовали или добавляли кросс. Значения: -1 - не установлен; 1 - кросс БИТЫЙ; 0 - кросс ВЕРНЫЙ | 
**rm** | **int** | Rating minus / Количество голосов участников и программных обработчиков, что кросс БИТЫЙ | 
**rp** | **int** | Rating plus / Количество голосов участников и программных обработчиков, что кросс ВЕРНЫЙ | 
**pi** | **int** | Ссылка на ДЕТАЛЬ (внешний ключ на productList.i) | 
**mfi** | **int** | Manufacturer index / Ссылка на БРЕНД (внешний ключ на manufacturerList.i) | 
**ns** | **str** | Стандартизированный НОМЕР | 
**pai** | **int** | Ссылка на КРОСС_ДЕТАЛЬ (внешний ключ на productList.i) | 
**mfai** | **int** | Manufacturer analog index / Ссылка на КРОСС_БРЕНД (внешний ключ на manufacturerList.i) | 
**nsa** | **str** | Стандартизированный КРОСС_НОМЕР | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


