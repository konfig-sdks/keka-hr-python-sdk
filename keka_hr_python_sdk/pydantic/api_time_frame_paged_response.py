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

from keka_hr_python_sdk.pydantic.api_time_frame import APITimeFrame
from keka_hr_python_sdk.pydantic.api_time_frame_paged_response_errors import APITimeFramePagedResponseErrors

class APITimeFramePagedResponse(BaseModel):
    # Gets or sets a value indicating whether this Keka.API.Web.Core.Response`1 is succeeded.
    succeeded: typing.Optional[bool] = Field(None, alias='succeeded')

    # Gets or sets the message.
    message: typing.Optional[typing.Optional[str]] = Field(None, alias='message')

    errors: typing.Optional[APITimeFramePagedResponseErrors] = Field(None, alias='errors')

    # Gets or sets the data.
    data: typing.Optional[typing.Optional[typing.List[APITimeFrame]]] = Field(None, alias='data')

    # Gets or sets the page number.
    page_number: typing.Optional[int] = Field(None, alias='pageNumber')

    # Gets or sets the size of the page.
    page_size: typing.Optional[int] = Field(None, alias='pageSize')

    # Gets or sets the first page.
    first_page: typing.Optional[typing.Optional[str]] = Field(None, alias='firstPage')

    # Gets or sets the last page.
    last_page: typing.Optional[typing.Optional[str]] = Field(None, alias='lastPage')

    # Gets or sets the total pages.
    total_pages: typing.Optional[int] = Field(None, alias='totalPages')

    # Gets or sets the total records.
    total_records: typing.Optional[int] = Field(None, alias='totalRecords')

    # Gets or sets the next page.
    next_page: typing.Optional[typing.Optional[str]] = Field(None, alias='nextPage')

    # Gets or sets the previous page.
    previous_page: typing.Optional[typing.Optional[str]] = Field(None, alias='previousPage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
