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

from keka_hr_python_sdk.pydantic.api_project_custom_attributes import APIProjectCustomAttributes
from keka_hr_python_sdk.pydantic.employee_lookup import EmployeeLookup
from keka_hr_python_sdk.pydantic.project_status import ProjectStatus

class APIProject(BaseModel):
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    client_id: typing.Optional[typing.Optional[str]] = Field(None, alias='clientId')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    code: typing.Optional[typing.Optional[str]] = Field(None, alias='code')

    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    end_date: typing.Optional[datetime] = Field(None, alias='endDate')

    status: typing.Optional[ProjectStatus] = Field(None, alias='status')

    project_managers: typing.Optional[typing.Optional[typing.List[EmployeeLookup]]] = Field(None, alias='projectManagers')

    is_billable: typing.Optional[bool] = Field(None, alias='isBillable')

    is_archived: typing.Optional[bool] = Field(None, alias='isArchived')

    custom_attributes: typing.Optional[APIProjectCustomAttributes] = Field(None, alias='customAttributes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
