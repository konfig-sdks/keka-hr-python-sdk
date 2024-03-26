# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from keka_hr_python_sdk.paths.hris_currencies.get import GetAll
from keka_hr_python_sdk.apis.tags.currency_api_raw import CurrencyApiRaw


class CurrencyApi(
    GetAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CurrencyApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CurrencyApiRaw(api_client)
