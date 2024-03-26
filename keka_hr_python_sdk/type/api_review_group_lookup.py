# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredAPIReviewGroupLookup(TypedDict):
    pass

class OptionalAPIReviewGroupLookup(TypedDict, total=False):
    id: typing.Optional[str]

    name: typing.Optional[str]

class APIReviewGroupLookup(RequiredAPIReviewGroupLookup, OptionalAPIReviewGroupLookup):
    pass
