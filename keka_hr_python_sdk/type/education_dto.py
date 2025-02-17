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


class RequiredEducationDTO(TypedDict):
    pass

class OptionalEducationDTO(TypedDict, total=False):
    # Gets or sets the degree.
    degree: typing.Optional[str]

    # Gets or sets the branch.
    branch: typing.Optional[str]

    # Gets or sets the date of joining.
    dateOfJoining: typing.Optional[str]

    # Gets or sets the date of completion.
    dateOfCompletion: typing.Optional[str]

    # Gets or sets the university.
    university: typing.Optional[str]

    # Gets or sets the location.
    location: typing.Optional[str]

class EducationDTO(RequiredEducationDTO, OptionalEducationDTO):
    pass
