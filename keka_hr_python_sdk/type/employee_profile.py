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

from keka_hr_python_sdk.type.account_status import AccountStatus
from keka_hr_python_sdk.type.address import Address
from keka_hr_python_sdk.type.blood_group import BloodGroup
from keka_hr_python_sdk.type.contingent_type import ContingentType
from keka_hr_python_sdk.type.custom_field import CustomField
from keka_hr_python_sdk.type.education import Education
from keka_hr_python_sdk.type.employee_lookup import EmployeeLookup
from keka_hr_python_sdk.type.employment_status import EmploymentStatus
from keka_hr_python_sdk.type.exit_status import ExitStatus
from keka_hr_python_sdk.type.exit_type import ExitType
from keka_hr_python_sdk.type.experience import Experience
from keka_hr_python_sdk.type.gender import Gender
from keka_hr_python_sdk.type.group_lookup import GroupLookup
from keka_hr_python_sdk.type.image import Image
from keka_hr_python_sdk.type.invitation_status import InvitationStatus
from keka_hr_python_sdk.type.lookup_info import LookupInfo
from keka_hr_python_sdk.type.marital_status import MaritalStatus
from keka_hr_python_sdk.type.relation import Relation
from keka_hr_python_sdk.type.time_type import TimeType
from keka_hr_python_sdk.type.worker_type import WorkerType

class RequiredEmployeeProfile(TypedDict):
    pass

class OptionalEmployeeProfile(TypedDict, total=False):
    id: typing.Optional[str]

    employeeNumber: typing.Optional[str]

    firstName: typing.Optional[str]

    middleName: typing.Optional[str]

    lastName: typing.Optional[str]

    displayName: typing.Optional[str]

    email: typing.Optional[str]

    city: typing.Optional[str]

    countryCode: typing.Optional[str]

    image: Image

    jobTitle: LookupInfo

    secondaryJobTitle: typing.Optional[str]

    reportsTo: EmployeeLookup

    l2Manager: EmployeeLookup

    dottedLineManager: EmployeeLookup

    contingentType: ContingentType

    timeType: TimeType

    workerType: WorkerType

    isPrivate: bool

    isProfileComplete: bool

    maritalStatus: MaritalStatus

    marriageDate: typing.Optional[datetime]

    gender: Gender

    joiningDate: datetime

    professionalSummary: typing.Optional[str]

    dateOfBirth: typing.Optional[datetime]

    resignationSubmittedDate: typing.Optional[datetime]

    exitDate: typing.Optional[datetime]

    employmentStatus: EmploymentStatus

    accountStatus: AccountStatus

    invitationStatus: InvitationStatus

    exitStatus: ExitStatus

    exitType: ExitType

    exitReason: typing.Optional[str]

    personalEmail: typing.Optional[str]

    workPhone: typing.Optional[str]

    homePhone: typing.Optional[str]

    mobilePhone: typing.Optional[str]

    bloodGroup: BloodGroup

    attendanceNumber: typing.Optional[str]

    probationEndDate: typing.Optional[datetime]

    currentAddress: Address

    permanentAddress: Address

    relations: typing.Optional[typing.List[Relation]]

    educationDetails: typing.Optional[typing.List[Education]]

    experienceDetails: typing.Optional[typing.List[Experience]]

    customFields: typing.Optional[typing.List[CustomField]]

    groups: typing.Optional[typing.List[GroupLookup]]

    leavePlanInfo: LookupInfo

    bandInfo: LookupInfo

    payGradeInfo: LookupInfo

    shiftPolicyInfo: LookupInfo

    weeklyOffPolicyInfo: LookupInfo

    captureSchemeInfo: LookupInfo

    trackingPolicyInfo: LookupInfo

    expensePolicyInfo: LookupInfo

    overtimePolicyInfo: LookupInfo

    identifier: typing.Optional[str]

class EmployeeProfile(RequiredEmployeeProfile, OptionalEmployeeProfile):
    pass
