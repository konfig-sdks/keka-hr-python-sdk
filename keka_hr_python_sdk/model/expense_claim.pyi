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


class ExpenseClaim(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'title':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            id = schemas.UUIDSchema
            employeeIdentifier = schemas.UUIDSchema
            
            
            class employeeName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employeeName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class claimNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'claimNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            submittedOn = schemas.DateTimeSchema
        
            @staticmethod
            def approvalStatus() -> typing.Type['ExpenseClaimApprovalStatus']:
                return ExpenseClaimApprovalStatus
            
            
            class expenses(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Expense']:
                        return Expense
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expenses':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "title": title,
                "id": id,
                "employeeIdentifier": employeeIdentifier,
                "employeeName": employeeName,
                "claimNumber": claimNumber,
                "submittedOn": submittedOn,
                "approvalStatus": approvalStatus,
                "expenses": expenses,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeIdentifier"]) -> MetaOapg.properties.employeeIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeName"]) -> MetaOapg.properties.employeeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claimNumber"]) -> MetaOapg.properties.claimNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedOn"]) -> MetaOapg.properties.submittedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalStatus"]) -> 'ExpenseClaimApprovalStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expenses"]) -> MetaOapg.properties.expenses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "employeeIdentifier", "employeeName", "claimNumber", "submittedOn", "approvalStatus", "expenses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeIdentifier"]) -> typing.Union[MetaOapg.properties.employeeIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeName"]) -> typing.Union[MetaOapg.properties.employeeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claimNumber"]) -> typing.Union[MetaOapg.properties.claimNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedOn"]) -> typing.Union[MetaOapg.properties.submittedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalStatus"]) -> typing.Union['ExpenseClaimApprovalStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expenses"]) -> typing.Union[MetaOapg.properties.expenses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "employeeIdentifier", "employeeName", "claimNumber", "submittedOn", "approvalStatus", "expenses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, None, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employeeIdentifier: typing.Union[MetaOapg.properties.employeeIdentifier, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employeeName: typing.Union[MetaOapg.properties.employeeName, None, str, schemas.Unset] = schemas.unset,
        claimNumber: typing.Union[MetaOapg.properties.claimNumber, None, str, schemas.Unset] = schemas.unset,
        submittedOn: typing.Union[MetaOapg.properties.submittedOn, str, datetime, schemas.Unset] = schemas.unset,
        approvalStatus: typing.Union['ExpenseClaimApprovalStatus', schemas.Unset] = schemas.unset,
        expenses: typing.Union[MetaOapg.properties.expenses, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseClaim':
        return super().__new__(
            cls,
            *args,
            title=title,
            id=id,
            employeeIdentifier=employeeIdentifier,
            employeeName=employeeName,
            claimNumber=claimNumber,
            submittedOn=submittedOn,
            approvalStatus=approvalStatus,
            expenses=expenses,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.expense import Expense
from keka_hr_python_sdk.model.expense_claim_approval_status import ExpenseClaimApprovalStatus
