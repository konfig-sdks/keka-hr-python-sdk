# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from keka_hr_python_sdk import schemas  # noqa: F401


class JobsGetApplicationFieldsResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['JobApplicationFieldsDTO']:
            return JobApplicationFieldsDTO

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['JobApplicationFieldsDTO'], typing.List['JobApplicationFieldsDTO']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'JobsGetApplicationFieldsResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'JobApplicationFieldsDTO':
        return super().__getitem__(i)

from keka_hr_python_sdk.model.job_application_fields_dto import JobApplicationFieldsDTO
