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


class BatchPagedResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    class represents paged response.
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
            def errors() -> typing.Type['BatchPagedResponseErrors']:
                return BatchPagedResponseErrors
            
            
            class data(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Batch']:
                        return Batch
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            pageNumber = schemas.Int32Schema
            pageSize = schemas.Int32Schema
            
            
            class firstPage(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'firstPage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class lastPage(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastPage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            totalPages = schemas.Int32Schema
            totalRecords = schemas.Int32Schema
            
            
            class nextPage(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nextPage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class previousPage(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'previousPage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "succeeded": succeeded,
                "message": message,
                "errors": errors,
                "data": data,
                "pageNumber": pageNumber,
                "pageSize": pageSize,
                "firstPage": firstPage,
                "lastPage": lastPage,
                "totalPages": totalPages,
                "totalRecords": totalRecords,
                "nextPage": nextPage,
                "previousPage": previousPage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["succeeded"]) -> MetaOapg.properties.succeeded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'BatchPagedResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstPage"]) -> MetaOapg.properties.firstPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastPage"]) -> MetaOapg.properties.lastPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalRecords"]) -> MetaOapg.properties.totalRecords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPage"]) -> MetaOapg.properties.nextPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousPage"]) -> MetaOapg.properties.previousPage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["succeeded", "message", "errors", "data", "pageNumber", "pageSize", "firstPage", "lastPage", "totalPages", "totalRecords", "nextPage", "previousPage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["succeeded"]) -> typing.Union[MetaOapg.properties.succeeded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['BatchPagedResponseErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> typing.Union[MetaOapg.properties.pageNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> typing.Union[MetaOapg.properties.pageSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstPage"]) -> typing.Union[MetaOapg.properties.firstPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastPage"]) -> typing.Union[MetaOapg.properties.lastPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> typing.Union[MetaOapg.properties.totalPages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalRecords"]) -> typing.Union[MetaOapg.properties.totalRecords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPage"]) -> typing.Union[MetaOapg.properties.nextPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousPage"]) -> typing.Union[MetaOapg.properties.previousPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["succeeded", "message", "errors", "data", "pageNumber", "pageSize", "firstPage", "lastPage", "totalPages", "totalRecords", "nextPage", "previousPage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        succeeded: typing.Union[MetaOapg.properties.succeeded, bool, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, None, str, schemas.Unset] = schemas.unset,
        errors: typing.Union['BatchPagedResponseErrors', schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, list, tuple, None, schemas.Unset] = schemas.unset,
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        firstPage: typing.Union[MetaOapg.properties.firstPage, None, str, schemas.Unset] = schemas.unset,
        lastPage: typing.Union[MetaOapg.properties.lastPage, None, str, schemas.Unset] = schemas.unset,
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalRecords: typing.Union[MetaOapg.properties.totalRecords, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nextPage: typing.Union[MetaOapg.properties.nextPage, None, str, schemas.Unset] = schemas.unset,
        previousPage: typing.Union[MetaOapg.properties.previousPage, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatchPagedResponse':
        return super().__new__(
            cls,
            *args,
            succeeded=succeeded,
            message=message,
            errors=errors,
            data=data,
            pageNumber=pageNumber,
            pageSize=pageSize,
            firstPage=firstPage,
            lastPage=lastPage,
            totalPages=totalPages,
            totalRecords=totalRecords,
            nextPage=nextPage,
            previousPage=previousPage,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.batch import Batch
from keka_hr_python_sdk.model.batch_paged_response_errors import BatchPagedResponseErrors
