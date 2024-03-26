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


class BillingInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "billingCurrencyId",
        }
        
        class properties:
            billingCurrencyId = schemas.StrSchema
        
            @staticmethod
            def billingAddress() -> typing.Type['Address']:
                return Address
            __annotations__ = {
                "billingCurrencyId": billingCurrencyId,
                "billingAddress": billingAddress,
            }
    
    billingCurrencyId: MetaOapg.properties.billingCurrencyId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingCurrencyId"]) -> MetaOapg.properties.billingCurrencyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingAddress"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["billingCurrencyId", "billingAddress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingCurrencyId"]) -> MetaOapg.properties.billingCurrencyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingAddress"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["billingCurrencyId", "billingAddress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        billingCurrencyId: typing.Union[MetaOapg.properties.billingCurrencyId, str, ],
        billingAddress: typing.Union['Address', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BillingInfo':
        return super().__new__(
            cls,
            *args,
            billingCurrencyId=billingCurrencyId,
            billingAddress=billingAddress,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.address import Address
