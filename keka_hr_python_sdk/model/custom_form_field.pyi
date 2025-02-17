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


class CustomFormField(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class question(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'question':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class answer(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'answer':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def multipleAnswers() -> typing.Type['CustomFormFieldMultipleAnswers']:
                return CustomFormFieldMultipleAnswers
            __annotations__ = {
                "question": question,
                "answer": answer,
                "multipleAnswers": multipleAnswers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer"]) -> MetaOapg.properties.answer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multipleAnswers"]) -> 'CustomFormFieldMultipleAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question", "answer", "multipleAnswers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> typing.Union[MetaOapg.properties.question, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer"]) -> typing.Union[MetaOapg.properties.answer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multipleAnswers"]) -> typing.Union['CustomFormFieldMultipleAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question", "answer", "multipleAnswers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        question: typing.Union[MetaOapg.properties.question, None, str, schemas.Unset] = schemas.unset,
        answer: typing.Union[MetaOapg.properties.answer, None, str, schemas.Unset] = schemas.unset,
        multipleAnswers: typing.Union['CustomFormFieldMultipleAnswers', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFormField':
        return super().__new__(
            cls,
            *args,
            question=question,
            answer=answer,
            multipleAnswers=multipleAnswers,
            _configuration=_configuration,
            **kwargs,
        )

from keka_hr_python_sdk.model.custom_form_field_multiple_answers import CustomFormFieldMultipleAnswers
