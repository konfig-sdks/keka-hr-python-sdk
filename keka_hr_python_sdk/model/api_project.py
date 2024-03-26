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


class APIProject(
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
            
            
            class clientId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clientId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class code(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'code':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
        
            @staticmethod
            def status() -> typing.Type['ProjectStatus']:
                return ProjectStatus
            
            
            class projectManagers(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmployeeLookup']:
                        return EmployeeLookup
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projectManagers':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            isBillable = schemas.BoolSchema
            isArchived = schemas.BoolSchema
        
            @staticmethod
            def customAttributes() -> typing.Type['APIProjectCustomAttributes']:
                return APIProjectCustomAttributes
            __annotations__ = {
                "id": id,
                "clientId": clientId,
                "name": name,
                "code": code,
                "startDate": startDate,
                "endDate": endDate,
                "status": status,
                "projectManagers": projectManagers,
                "isBillable": isBillable,
                "isArchived": isArchived,
                "customAttributes": customAttributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ProjectStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectManagers"]) -> MetaOapg.properties.projectManagers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isBillable"]) -> MetaOapg.properties.isBillable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isArchived"]) -> MetaOapg.properties.isArchived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customAttributes"]) -> 'APIProjectCustomAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "clientId", "name", "code", "startDate", "endDate", "status", "projectManagers", "isBillable", "isArchived", "customAttributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ProjectStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectManagers"]) -> typing.Union[MetaOapg.properties.projectManagers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isBillable"]) -> typing.Union[MetaOapg.properties.isBillable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isArchived"]) -> typing.Union[MetaOapg.properties.isArchived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customAttributes"]) -> typing.Union['APIProjectCustomAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "clientId", "name", "code", "startDate", "endDate", "status", "projectManagers", "isBillable", "isArchived", "customAttributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, None, str, schemas.Unset] = schemas.unset,
        clientId: typing.Union[MetaOapg.properties.clientId, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, None, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        status: typing.Union['ProjectStatus', schemas.Unset] = schemas.unset,
        projectManagers: typing.Union[MetaOapg.properties.projectManagers, list, tuple, None, schemas.Unset] = schemas.unset,
        isBillable: typing.Union[MetaOapg.properties.isBillable, bool, schemas.Unset] = schemas.unset,
        isArchived: typing.Union[MetaOapg.properties.isArchived, bool, schemas.Unset] = schemas.unset,
        customAttributes: typing.Union['APIProjectCustomAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIProject':
        return super().__new__(
            cls,
            *args,
            id=id,
            clientId=clientId,
            name=name,
            code=code,
            startDate=startDate,
            endDate=endDate,
            status=status,
            projectManagers=projectManagers,
            isBillable=isBillable,
            isArchived=isArchived,
            customAttributes=customAttributes,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.api_project_custom_attributes import APIProjectCustomAttributes
from keka_hr_python_sdk.model.employee_lookup import EmployeeLookup
from keka_hr_python_sdk.model.project_status import ProjectStatus
