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

from keka_hr_python_sdk.type.hiring_team_dto import HiringTeamDTO
from keka_hr_python_sdk.type.job_custom_field_dto import JobCustomFieldDTO
from keka_hr_python_sdk.type.job_status import JobStatus
from keka_hr_python_sdk.type.location_dto import LocationDTO

class RequiredJobDTO(TypedDict):
    pass

class OptionalJobDTO(TypedDict, total=False):
    title: typing.Optional[str]

    description: typing.Optional[str]

    id: typing.Optional[str]

    noOfOpenings: typing.Optional[str]

    departmentName: typing.Optional[str]

    jobType: typing.Optional[str]

    isReferralEnabled: bool

    isCreatedFromRequisition: bool

    requisitionIdentifier: typing.Optional[str]

    canAllowInternalEmployees: bool

    orgJobId: typing.Optional[str]

    jobLocations: typing.Optional[typing.List[LocationDTO]]

    hiringTeam: typing.Optional[typing.List[HiringTeamDTO]]

    careerPortalUrl: typing.Optional[str]

    targetHireDate: typing.Optional[str]

    status: JobStatus

    createdOn: typing.Optional[str]

    publishedOn: typing.Optional[str]

    experience: typing.Optional[str]

    customFields: typing.Optional[typing.List[JobCustomFieldDTO]]

class JobDTO(RequiredJobDTO, OptionalJobDTO):
    pass
