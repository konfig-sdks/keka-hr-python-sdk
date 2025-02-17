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

from keka_hr_python_sdk.pydantic.asset_status import AssetStatus
from keka_hr_python_sdk.pydantic.employee_lookup import EmployeeLookup

class Asset(BaseModel):
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    asset_name: typing.Optional[typing.Optional[str]] = Field(None, alias='assetName')

    asset_id: typing.Optional[typing.Optional[str]] = Field(None, alias='assetId')

    status: typing.Optional[AssetStatus] = Field(None, alias='status')

    asset_category_id: typing.Optional[typing.Optional[str]] = Field(None, alias='assetCategoryId')

    asset_type_id: typing.Optional[typing.Optional[str]] = Field(None, alias='assetTypeId')

    asset_condition_id: typing.Optional[typing.Optional[str]] = Field(None, alias='assetConditionId')

    assigned_to: typing.Optional[EmployeeLookup] = Field(None, alias='assignedTo')

    assigned_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='assignedOn')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
