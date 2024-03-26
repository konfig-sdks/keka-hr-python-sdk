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


class Education(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class degree(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'degree':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class branch(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'branch':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class university(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'university':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            cgpa = schemas.Float64Schema
            
            
            class yearOfJoining(
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
                ) -> 'yearOfJoining':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class yearOfCompletion(
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
                ) -> 'yearOfCompletion':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customFields(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomField']:
                        return CustomField
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customFields':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "degree": degree,
                "branch": branch,
                "university": university,
                "cgpa": cgpa,
                "yearOfJoining": yearOfJoining,
                "yearOfCompletion": yearOfCompletion,
                "customFields": customFields,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["degree"]) -> MetaOapg.properties.degree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branch"]) -> MetaOapg.properties.branch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["university"]) -> MetaOapg.properties.university: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cgpa"]) -> MetaOapg.properties.cgpa: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearOfJoining"]) -> MetaOapg.properties.yearOfJoining: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearOfCompletion"]) -> MetaOapg.properties.yearOfCompletion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> MetaOapg.properties.customFields: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "degree", "branch", "university", "cgpa", "yearOfJoining", "yearOfCompletion", "customFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["degree"]) -> typing.Union[MetaOapg.properties.degree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branch"]) -> typing.Union[MetaOapg.properties.branch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["university"]) -> typing.Union[MetaOapg.properties.university, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cgpa"]) -> typing.Union[MetaOapg.properties.cgpa, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearOfJoining"]) -> typing.Union[MetaOapg.properties.yearOfJoining, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearOfCompletion"]) -> typing.Union[MetaOapg.properties.yearOfCompletion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union[MetaOapg.properties.customFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "degree", "branch", "university", "cgpa", "yearOfJoining", "yearOfCompletion", "customFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, None, str, schemas.Unset] = schemas.unset,
        degree: typing.Union[MetaOapg.properties.degree, None, str, schemas.Unset] = schemas.unset,
        branch: typing.Union[MetaOapg.properties.branch, None, str, schemas.Unset] = schemas.unset,
        university: typing.Union[MetaOapg.properties.university, None, str, schemas.Unset] = schemas.unset,
        cgpa: typing.Union[MetaOapg.properties.cgpa, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        yearOfJoining: typing.Union[MetaOapg.properties.yearOfJoining, None, str, datetime, schemas.Unset] = schemas.unset,
        yearOfCompletion: typing.Union[MetaOapg.properties.yearOfCompletion, None, str, datetime, schemas.Unset] = schemas.unset,
        customFields: typing.Union[MetaOapg.properties.customFields, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Education':
        return super().__new__(
            cls,
            *args,
            id=id,
            degree=degree,
            branch=branch,
            university=university,
            cgpa=cgpa,
            yearOfJoining=yearOfJoining,
            yearOfCompletion=yearOfCompletion,
            customFields=customFields,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.custom_field import CustomField
