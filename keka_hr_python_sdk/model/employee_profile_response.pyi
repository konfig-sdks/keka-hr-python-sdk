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


class EmployeeProfileResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    class represents response.
    """


    class MetaOapg:
        
        class properties:
            succeeded = schemas.BoolSchema
            
            
            class message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def errors() -> typing.Type['EmployeeProfileResponseErrors']:
                return EmployeeProfileResponseErrors
        
            @staticmethod
            def items() -> typing.Type['EmployeeProfile']:
                return EmployeeProfile
            __annotations__ = {
                "succeeded": succeeded,
                "message": message,
                "errors": errors,
                "items": items,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["succeeded"]) -> MetaOapg.properties.succeeded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'EmployeeProfileResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> 'EmployeeProfile': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["succeeded", "message", "errors", "items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["succeeded"]) -> typing.Union[MetaOapg.properties.succeeded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['EmployeeProfileResponseErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union['EmployeeProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["succeeded", "message", "errors", "items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        succeeded: typing.Union[MetaOapg.properties.succeeded, bool, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, None, str, schemas.Unset] = schemas.unset,
        errors: typing.Union['EmployeeProfileResponseErrors', schemas.Unset] = schemas.unset,
        items: typing.Union['EmployeeProfile', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeProfileResponse':
        return super().__new__(
            cls,
            *args,
            succeeded=succeeded,
            message=message,
            errors=errors,
            items=items,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.employee_profile import EmployeeProfile
from keka_hr_python_sdk.model.employee_profile_response_errors import EmployeeProfileResponseErrors
