# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from twitter_openapi_python_generated.models.timeline_add_entry import TimelineAddEntry

class TimelineReplaceEntry(BaseModel):
    """
    TimelineReplaceEntry
    """
    entry: TimelineAddEntry = Field(...)
    entry_id_to_replace: StrictStr = Field(...)
    type: StrictStr = Field(...)
    __properties = ["entry", "entry_id_to_replace", "type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TimelineReplaceEntry:
        """Create an instance of TimelineReplaceEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entry
        if self.entry:
            _dict['entry'] = self.entry.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineReplaceEntry:
        """Create an instance of TimelineReplaceEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineReplaceEntry.parse_obj(obj)

        _obj = TimelineReplaceEntry.parse_obj({
            "entry": TimelineAddEntry.from_dict(obj.get("entry")) if obj.get("entry") is not None else None,
            "entry_id_to_replace": obj.get("entry_id_to_replace"),
            "type": obj.get("type")
        })
        return _obj
