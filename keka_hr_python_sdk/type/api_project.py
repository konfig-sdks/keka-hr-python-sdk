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

from keka_hr_python_sdk.type.api_project_custom_attributes import APIProjectCustomAttributes
from keka_hr_python_sdk.type.employee_lookup import EmployeeLookup
from keka_hr_python_sdk.type.project_status import ProjectStatus

class RequiredAPIProject(TypedDict):
    pass

class OptionalAPIProject(TypedDict, total=False):
    id: typing.Optional[str]

    clientId: typing.Optional[str]

    name: typing.Optional[str]

    code: typing.Optional[str]

    startDate: datetime

    endDate: datetime

    status: ProjectStatus

    projectManagers: typing.Optional[typing.List[EmployeeLookup]]

    isBillable: bool

    isArchived: bool

    customAttributes: typing.Optional[APIProjectCustomAttributes]

class APIProject(RequiredAPIProject, OptionalAPIProject):
    pass
