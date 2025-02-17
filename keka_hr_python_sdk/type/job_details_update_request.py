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

from keka_hr_python_sdk.type.job_details_update_request_custom_fields import JobDetailsUpdateRequestCustomFields
from keka_hr_python_sdk.type.time_type import TimeType

class RequiredJobDetailsUpdateRequest(TypedDict):
    pass

class OptionalJobDetailsUpdateRequest(TypedDict, total=False):
    employeeNumber: typing.Optional[str]

    location: typing.Optional[str]

    businessUnit: typing.Optional[str]

    department: typing.Optional[str]

    jobTitle: typing.Optional[str]

    reportingManager: typing.Optional[str]

    attendanceNumber: typing.Optional[str]

    timeType: TimeType

    attendanceCaptureScheme: typing.Optional[str]

    expensePolicy: typing.Optional[str]

    noticePeriod: typing.Optional[str]

    holidayList: typing.Optional[str]

    costCenter: typing.Optional[str]

    payBand: typing.Optional[str]

    payGrade: typing.Optional[str]

    customFields: typing.Optional[JobDetailsUpdateRequestCustomFields]

class JobDetailsUpdateRequest(RequiredJobDetailsUpdateRequest, OptionalJobDetailsUpdateRequest):
    pass
