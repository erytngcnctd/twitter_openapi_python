# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class MediaVideoInfoVariant(BaseModel):
    """
    MediaVideoInfoVariant
    """
    bitrate: Optional[StrictInt] = None
    content_type: StrictStr = Field(...)
    url: StrictStr = Field(...)
    __properties = ["bitrate", "content_type", "url"]

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
    def from_json(cls, json_str: str) -> MediaVideoInfoVariant:
        """Create an instance of MediaVideoInfoVariant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaVideoInfoVariant:
        """Create an instance of MediaVideoInfoVariant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MediaVideoInfoVariant.parse_obj(obj)

        _obj = MediaVideoInfoVariant.parse_obj({
            "bitrate": obj.get("bitrate"),
            "content_type": obj.get("content_type"),
            "url": obj.get("url")
        })
        return _obj

