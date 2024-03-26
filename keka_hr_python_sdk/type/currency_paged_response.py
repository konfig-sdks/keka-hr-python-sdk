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

from keka_hr_python_sdk.type.currency import Currency
from keka_hr_python_sdk.type.currency_paged_response_errors import CurrencyPagedResponseErrors

class RequiredCurrencyPagedResponse(TypedDict):
    pass

class OptionalCurrencyPagedResponse(TypedDict, total=False):
    # Gets or sets a value indicating whether this Keka.API.Web.Core.Response`1 is succeeded.
    succeeded: bool

    # Gets or sets the message.
    message: typing.Optional[str]

    errors: typing.Optional[CurrencyPagedResponseErrors]

    # Gets or sets the data.
    data: typing.Optional[typing.List[Currency]]

    # Gets or sets the page number.
    pageNumber: int

    # Gets or sets the size of the page.
    pageSize: int

    # Gets or sets the first page.
    firstPage: typing.Optional[str]

    # Gets or sets the last page.
    lastPage: typing.Optional[str]

    # Gets or sets the total pages.
    totalPages: int

    # Gets or sets the total records.
    totalRecords: int

    # Gets or sets the next page.
    nextPage: typing.Optional[str]

    # Gets or sets the previous page.
    previousPage: typing.Optional[str]

class CurrencyPagedResponse(RequiredCurrencyPagedResponse, OptionalCurrencyPagedResponse):
    pass
