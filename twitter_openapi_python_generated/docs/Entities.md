# Entities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashtags** | **List[object]** |  | 
**media** | [**List[Media]**](Media.md) |  | [optional] 
**symbols** | **List[object]** |  | 
**urls** | [**List[Url]**](Url.md) |  | 
**user_mentions** | **List[object]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.entities import Entities

# TODO update the JSON string below
json = "{}"
# create an instance of Entities from a JSON string
entities_instance = Entities.from_json(json)
# print the JSON string representation of the object
print Entities.to_json()

# convert the object into a dict
entities_dict = entities_instance.to_dict()
# create an instance of Entities from a dict
entities_form_dict = entities.from_dict(entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

