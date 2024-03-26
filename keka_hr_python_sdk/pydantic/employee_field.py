# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from keka_hr_python_sdk.pydantic.field_item import FieldItem

class EmployeeField(BaseModel):
    profile_fields: typing.Optional[typing.Optional[typing.List[FieldItem]]] = Field(None, alias='profileFields')

    job_fields: typing.Optional[typing.Optional[typing.List[FieldItem]]] = Field(None, alias='jobFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
