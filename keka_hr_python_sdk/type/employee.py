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

from keka_hr_python_sdk.type.gender import Gender

class RequiredEmployee(TypedDict):
    displayName: str

    firstName: str

    lastName: str

    email: str

    gender: Gender

    dateOfBirth: datetime

    dateJoined: datetime

    department: str

    businessUnit: str

    jobTitle: str

    location: str

class OptionalEmployee(TypedDict, total=False):
    employeeNumber: typing.Optional[str]

    middleName: typing.Optional[str]

    mobileNumber: typing.Optional[str]

    secondaryJobTitle: typing.Optional[str]

class Employee(RequiredEmployee, OptionalEmployee):
    pass
