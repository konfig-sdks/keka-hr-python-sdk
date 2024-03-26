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


class APIProjectAllocation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
        
            @staticmethod
            def employee() -> typing.Type['EmployeeLookup']:
                return EmployeeLookup
            startDate = schemas.DateTimeSchema
            
            
            class endDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'endDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            allocationPercentage = schemas.Int32Schema
        
            @staticmethod
            def billingRole() -> typing.Type['APILookup']:
                return APILookup
        
            @staticmethod
            def billingRate() -> typing.Type['BillingRateLookup']:
                return BillingRateLookup
            __annotations__ = {
                "id": id,
                "employee": employee,
                "startDate": startDate,
                "endDate": endDate,
                "allocationPercentage": allocationPercentage,
                "billingRole": billingRole,
                "billingRate": billingRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'EmployeeLookup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allocationPercentage"]) -> MetaOapg.properties.allocationPercentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingRole"]) -> 'APILookup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingRate"]) -> 'BillingRateLookup': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "employee", "startDate", "endDate", "allocationPercentage", "billingRole", "billingRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['EmployeeLookup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allocationPercentage"]) -> typing.Union[MetaOapg.properties.allocationPercentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingRole"]) -> typing.Union['APILookup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingRate"]) -> typing.Union['BillingRateLookup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "employee", "startDate", "endDate", "allocationPercentage", "billingRole", "billingRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employee: typing.Union['EmployeeLookup', schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, None, str, datetime, schemas.Unset] = schemas.unset,
        allocationPercentage: typing.Union[MetaOapg.properties.allocationPercentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        billingRole: typing.Union['APILookup', schemas.Unset] = schemas.unset,
        billingRate: typing.Union['BillingRateLookup', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIProjectAllocation':
        return super().__new__(
            cls,
            *args,
            id=id,
            employee=employee,
            startDate=startDate,
            endDate=endDate,
            allocationPercentage=allocationPercentage,
            billingRole=billingRole,
            billingRate=billingRate,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.api_lookup import APILookup
from keka_hr_python_sdk.model.billing_rate_lookup import BillingRateLookup
from keka_hr_python_sdk.model.employee_lookup import EmployeeLookup
