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


class JobApplicationDetailsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class jobHiringStageId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jobHiringStageId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class movedtoStageOn(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'movedtoStageOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def screeningQuestionsResponse() -> typing.Type['JobApplicationDetailsDTOScreeningQuestionsResponse']:
                return JobApplicationDetailsDTOScreeningQuestionsResponse
            
            
            class appliedOn(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'appliedOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def status() -> typing.Type['ApplicationStatus']:
                return ApplicationStatus
            
            
            class sourcedBy(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourcedBy':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class sourceTitle(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceTitle':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class assignedTo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignedTo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class assignedOn(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignedOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "jobHiringStageId": jobHiringStageId,
                "movedtoStageOn": movedtoStageOn,
                "screeningQuestionsResponse": screeningQuestionsResponse,
                "appliedOn": appliedOn,
                "status": status,
                "sourcedBy": sourcedBy,
                "sourceTitle": sourceTitle,
                "assignedTo": assignedTo,
                "assignedOn": assignedOn,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobHiringStageId"]) -> MetaOapg.properties.jobHiringStageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedtoStageOn"]) -> MetaOapg.properties.movedtoStageOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["screeningQuestionsResponse"]) -> 'JobApplicationDetailsDTOScreeningQuestionsResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appliedOn"]) -> MetaOapg.properties.appliedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ApplicationStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourcedBy"]) -> MetaOapg.properties.sourcedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceTitle"]) -> MetaOapg.properties.sourceTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignedTo"]) -> MetaOapg.properties.assignedTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignedOn"]) -> MetaOapg.properties.assignedOn: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobHiringStageId", "movedtoStageOn", "screeningQuestionsResponse", "appliedOn", "status", "sourcedBy", "sourceTitle", "assignedTo", "assignedOn", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobHiringStageId"]) -> typing.Union[MetaOapg.properties.jobHiringStageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedtoStageOn"]) -> typing.Union[MetaOapg.properties.movedtoStageOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["screeningQuestionsResponse"]) -> typing.Union['JobApplicationDetailsDTOScreeningQuestionsResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appliedOn"]) -> typing.Union[MetaOapg.properties.appliedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ApplicationStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourcedBy"]) -> typing.Union[MetaOapg.properties.sourcedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceTitle"]) -> typing.Union[MetaOapg.properties.sourceTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignedTo"]) -> typing.Union[MetaOapg.properties.assignedTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignedOn"]) -> typing.Union[MetaOapg.properties.assignedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobHiringStageId", "movedtoStageOn", "screeningQuestionsResponse", "appliedOn", "status", "sourcedBy", "sourceTitle", "assignedTo", "assignedOn", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jobHiringStageId: typing.Union[MetaOapg.properties.jobHiringStageId, None, str, schemas.Unset] = schemas.unset,
        movedtoStageOn: typing.Union[MetaOapg.properties.movedtoStageOn, None, str, schemas.Unset] = schemas.unset,
        screeningQuestionsResponse: typing.Union['JobApplicationDetailsDTOScreeningQuestionsResponse', schemas.Unset] = schemas.unset,
        appliedOn: typing.Union[MetaOapg.properties.appliedOn, None, str, schemas.Unset] = schemas.unset,
        status: typing.Union['ApplicationStatus', schemas.Unset] = schemas.unset,
        sourcedBy: typing.Union[MetaOapg.properties.sourcedBy, None, str, schemas.Unset] = schemas.unset,
        sourceTitle: typing.Union[MetaOapg.properties.sourceTitle, None, str, schemas.Unset] = schemas.unset,
        assignedTo: typing.Union[MetaOapg.properties.assignedTo, None, str, schemas.Unset] = schemas.unset,
        assignedOn: typing.Union[MetaOapg.properties.assignedOn, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobApplicationDetailsDTO':
        return super().__new__(
            cls,
            *args,
            jobHiringStageId=jobHiringStageId,
            movedtoStageOn=movedtoStageOn,
            screeningQuestionsResponse=screeningQuestionsResponse,
            appliedOn=appliedOn,
            status=status,
            sourcedBy=sourcedBy,
            sourceTitle=sourceTitle,
            assignedTo=assignedTo,
            assignedOn=assignedOn,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.application_status import ApplicationStatus
from keka_hr_python_sdk.model.job_application_details_dto_screening_questions_response import JobApplicationDetailsDTOScreeningQuestionsResponse
