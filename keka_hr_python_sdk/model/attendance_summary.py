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


class AttendanceSummary(
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
            
            
            class employeeNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employeeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class employeeIdentifier(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employeeIdentifier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            attendanceDate = schemas.DateTimeSchema
        
            @staticmethod
            def dayType() -> typing.Type['AttendanceDayType']:
                return AttendanceDayType
        
            @staticmethod
            def leaveDayStatus() -> typing.Type['LeaveDayStatus']:
                return LeaveDayStatus
            shiftStartTime = schemas.DateTimeSchema
            shiftEndTime = schemas.DateTimeSchema
            shiftDuration = schemas.Float64Schema
            shiftBreakDuration = schemas.Float64Schema
            shiftEffectiveDuration = schemas.Float64Schema
            totalGrossHours = schemas.Float64Schema
            totalEffectiveHours = schemas.Float64Schema
            totalBreakDuration = schemas.Float64Schema
            totalEffectiveOvertimeDuration = schemas.Float64Schema
            totalGrossOvertimeDuration = schemas.Float64Schema
        
            @staticmethod
            def firstInOfTheDay() -> typing.Type['AttendanceTimeEntry']:
                return AttendanceTimeEntry
        
            @staticmethod
            def lastOutOfTheDay() -> typing.Type['AttendanceTimeEntry']:
                return AttendanceTimeEntry
            __annotations__ = {
                "id": id,
                "employeeNumber": employeeNumber,
                "employeeIdentifier": employeeIdentifier,
                "attendanceDate": attendanceDate,
                "dayType": dayType,
                "leaveDayStatus": leaveDayStatus,
                "shiftStartTime": shiftStartTime,
                "shiftEndTime": shiftEndTime,
                "shiftDuration": shiftDuration,
                "shiftBreakDuration": shiftBreakDuration,
                "shiftEffectiveDuration": shiftEffectiveDuration,
                "totalGrossHours": totalGrossHours,
                "totalEffectiveHours": totalEffectiveHours,
                "totalBreakDuration": totalBreakDuration,
                "totalEffectiveOvertimeDuration": totalEffectiveOvertimeDuration,
                "totalGrossOvertimeDuration": totalGrossOvertimeDuration,
                "firstInOfTheDay": firstInOfTheDay,
                "lastOutOfTheDay": lastOutOfTheDay,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeIdentifier"]) -> MetaOapg.properties.employeeIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendanceDate"]) -> MetaOapg.properties.attendanceDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayType"]) -> 'AttendanceDayType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leaveDayStatus"]) -> 'LeaveDayStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftStartTime"]) -> MetaOapg.properties.shiftStartTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftEndTime"]) -> MetaOapg.properties.shiftEndTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftDuration"]) -> MetaOapg.properties.shiftDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftBreakDuration"]) -> MetaOapg.properties.shiftBreakDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftEffectiveDuration"]) -> MetaOapg.properties.shiftEffectiveDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalGrossHours"]) -> MetaOapg.properties.totalGrossHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEffectiveHours"]) -> MetaOapg.properties.totalEffectiveHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalBreakDuration"]) -> MetaOapg.properties.totalBreakDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEffectiveOvertimeDuration"]) -> MetaOapg.properties.totalEffectiveOvertimeDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalGrossOvertimeDuration"]) -> MetaOapg.properties.totalGrossOvertimeDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstInOfTheDay"]) -> 'AttendanceTimeEntry': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastOutOfTheDay"]) -> 'AttendanceTimeEntry': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "employeeNumber", "employeeIdentifier", "attendanceDate", "dayType", "leaveDayStatus", "shiftStartTime", "shiftEndTime", "shiftDuration", "shiftBreakDuration", "shiftEffectiveDuration", "totalGrossHours", "totalEffectiveHours", "totalBreakDuration", "totalEffectiveOvertimeDuration", "totalGrossOvertimeDuration", "firstInOfTheDay", "lastOutOfTheDay", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeIdentifier"]) -> typing.Union[MetaOapg.properties.employeeIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendanceDate"]) -> typing.Union[MetaOapg.properties.attendanceDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayType"]) -> typing.Union['AttendanceDayType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leaveDayStatus"]) -> typing.Union['LeaveDayStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftStartTime"]) -> typing.Union[MetaOapg.properties.shiftStartTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftEndTime"]) -> typing.Union[MetaOapg.properties.shiftEndTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftDuration"]) -> typing.Union[MetaOapg.properties.shiftDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftBreakDuration"]) -> typing.Union[MetaOapg.properties.shiftBreakDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftEffectiveDuration"]) -> typing.Union[MetaOapg.properties.shiftEffectiveDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalGrossHours"]) -> typing.Union[MetaOapg.properties.totalGrossHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEffectiveHours"]) -> typing.Union[MetaOapg.properties.totalEffectiveHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalBreakDuration"]) -> typing.Union[MetaOapg.properties.totalBreakDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEffectiveOvertimeDuration"]) -> typing.Union[MetaOapg.properties.totalEffectiveOvertimeDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalGrossOvertimeDuration"]) -> typing.Union[MetaOapg.properties.totalGrossOvertimeDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstInOfTheDay"]) -> typing.Union['AttendanceTimeEntry', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastOutOfTheDay"]) -> typing.Union['AttendanceTimeEntry', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "employeeNumber", "employeeIdentifier", "attendanceDate", "dayType", "leaveDayStatus", "shiftStartTime", "shiftEndTime", "shiftDuration", "shiftBreakDuration", "shiftEffectiveDuration", "totalGrossHours", "totalEffectiveHours", "totalBreakDuration", "totalEffectiveOvertimeDuration", "totalGrossOvertimeDuration", "firstInOfTheDay", "lastOutOfTheDay", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, None, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, None, str, schemas.Unset] = schemas.unset,
        employeeIdentifier: typing.Union[MetaOapg.properties.employeeIdentifier, None, str, schemas.Unset] = schemas.unset,
        attendanceDate: typing.Union[MetaOapg.properties.attendanceDate, str, datetime, schemas.Unset] = schemas.unset,
        dayType: typing.Union['AttendanceDayType', schemas.Unset] = schemas.unset,
        leaveDayStatus: typing.Union['LeaveDayStatus', schemas.Unset] = schemas.unset,
        shiftStartTime: typing.Union[MetaOapg.properties.shiftStartTime, str, datetime, schemas.Unset] = schemas.unset,
        shiftEndTime: typing.Union[MetaOapg.properties.shiftEndTime, str, datetime, schemas.Unset] = schemas.unset,
        shiftDuration: typing.Union[MetaOapg.properties.shiftDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        shiftBreakDuration: typing.Union[MetaOapg.properties.shiftBreakDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        shiftEffectiveDuration: typing.Union[MetaOapg.properties.shiftEffectiveDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalGrossHours: typing.Union[MetaOapg.properties.totalGrossHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalEffectiveHours: typing.Union[MetaOapg.properties.totalEffectiveHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalBreakDuration: typing.Union[MetaOapg.properties.totalBreakDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalEffectiveOvertimeDuration: typing.Union[MetaOapg.properties.totalEffectiveOvertimeDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalGrossOvertimeDuration: typing.Union[MetaOapg.properties.totalGrossOvertimeDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        firstInOfTheDay: typing.Union['AttendanceTimeEntry', schemas.Unset] = schemas.unset,
        lastOutOfTheDay: typing.Union['AttendanceTimeEntry', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttendanceSummary':
        return super().__new__(
            cls,
            *args,
            id=id,
            employeeNumber=employeeNumber,
            employeeIdentifier=employeeIdentifier,
            attendanceDate=attendanceDate,
            dayType=dayType,
            leaveDayStatus=leaveDayStatus,
            shiftStartTime=shiftStartTime,
            shiftEndTime=shiftEndTime,
            shiftDuration=shiftDuration,
            shiftBreakDuration=shiftBreakDuration,
            shiftEffectiveDuration=shiftEffectiveDuration,
            totalGrossHours=totalGrossHours,
            totalEffectiveHours=totalEffectiveHours,
            totalBreakDuration=totalBreakDuration,
            totalEffectiveOvertimeDuration=totalEffectiveOvertimeDuration,
            totalGrossOvertimeDuration=totalGrossOvertimeDuration,
            firstInOfTheDay=firstInOfTheDay,
            lastOutOfTheDay=lastOutOfTheDay,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.attendance_day_type import AttendanceDayType
from keka_hr_python_sdk.model.attendance_time_entry import AttendanceTimeEntry
from keka_hr_python_sdk.model.leave_day_status import LeaveDayStatus
