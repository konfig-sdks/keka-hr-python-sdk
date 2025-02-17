# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from keka_hr_python_sdk.paths.hris_employees.post import CreateEmployee
from keka_hr_python_sdk.paths.hris_employees.get import GetAll
from keka_hr_python_sdk.paths.hris_employees_updatefields.get import GetAllUpdateFields
from keka_hr_python_sdk.paths.hris_employees_id.get import GetById
from keka_hr_python_sdk.paths.hris_employees_id_jobdetails.put import UpdateJobDetails
from keka_hr_python_sdk.paths.hris_employees_id_personaldetails.put import UpdatePersonalDetails
from keka_hr_python_sdk.apis.tags.employees_api_raw import EmployeesApiRaw


class EmployeesApi(
    CreateEmployee,
    GetAll,
    GetAllUpdateFields,
    GetById,
    UpdateJobDetails,
    UpdatePersonalDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeesApiRaw(api_client)
