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

from keka_hr_python_sdk.pydantic.payment_status import PaymentStatus

class EmployeePayment(BaseModel):
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    employee_number: typing.Optional[typing.Optional[str]] = Field(None, alias='employeeNumber')

    employee_name: typing.Optional[typing.Optional[str]] = Field(None, alias='employeeName')

    for_period: typing.Optional[typing.Optional[str]] = Field(None, alias='forPeriod')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    salary_payment_mode: typing.Optional[typing.Optional[str]] = Field(None, alias='salaryPaymentMode')

    bank_name: typing.Optional[typing.Optional[str]] = Field(None, alias='bankName')

    ifsc_code: typing.Optional[typing.Optional[str]] = Field(None, alias='ifscCode')

    account_number: typing.Optional[typing.Optional[str]] = Field(None, alias='accountNumber')

    status: typing.Optional[PaymentStatus] = Field(None, alias='status')

    identifier: typing.Optional[typing.Optional[str]] = Field(None, alias='identifier')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
