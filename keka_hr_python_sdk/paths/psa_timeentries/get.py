# coding: utf-8

"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from keka_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from keka_hr_python_sdk.api_response import AsyncGeneratorResponse
from keka_hr_python_sdk import api_client, exceptions
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

from keka_hr_python_sdk.model.api_timesheet_entry_paged_response import APITimesheetEntryPagedResponse as APITimesheetEntryPagedResponseSchema

from keka_hr_python_sdk.type.api_timesheet_entry_paged_response import APITimesheetEntryPagedResponse

from ...api_client import Dictionary
from keka_hr_python_sdk.pydantic.api_timesheet_entry_paged_response import APITimesheetEntryPagedResponse as APITimesheetEntryPagedResponsePydantic

from . import path

# Query params
ModelFromSchema = schemas.DateTimeSchema
ToSchema = schemas.DateTimeSchema
EmployeeIdsSchema = schemas.StrSchema
ProjectIdsSchema = schemas.StrSchema
TaskIdsSchema = schemas.StrSchema
PageNumberSchema = schemas.Int32Schema
PageSizeSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'from': typing.Union[ModelFromSchema, str, datetime, ],
        'to': typing.Union[ToSchema, str, datetime, ],
        'employeeIds': typing.Union[EmployeeIdsSchema, str, ],
        'projectIds': typing.Union[ProjectIdsSchema, str, ],
        'taskIds': typing.Union[TaskIdsSchema, str, ],
        'pageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    explode=True,
)
request_query_employee_ids = api_client.QueryParameter(
    name="employeeIds",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdsSchema,
    explode=True,
)
request_query_project_ids = api_client.QueryParameter(
    name="projectIds",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectIdsSchema,
    explode=True,
)
request_query_task_ids = api_client.QueryParameter(
    name="taskIds",
    style=api_client.ParameterStyle.FORM,
    schema=TaskIdsSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="pageNumber",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = APITimesheetEntryPagedResponseSchema
SchemaFor200ResponseBodyTextJson = APITimesheetEntryPagedResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: APITimesheetEntryPagedResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: APITimesheetEntryPagedResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _get_between_dates_mapped_args(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if employee_ids is not None:
            _query_params["employeeIds"] = employee_ids
        if project_ids is not None:
            _query_params["projectIds"] = project_ids
        if task_ids is not None:
            _query_params["taskIds"] = task_ids
        if page_number is not None:
            _query_params["pageNumber"] = page_number
        if page_size is not None:
            _query_params["pageSize"] = page_size
        args.query = _query_params
        return args

    async def _aget_between_dates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get project timesheet entries.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_employee_ids,
            request_query_project_ids,
            request_query_task_ids,
            request_query_page_number,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/psa/timeentries',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_between_dates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get project timesheet entries.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_employee_ids,
            request_query_project_ids,
            request_query_task_ids,
            request_query_page_number,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/psa/timeentries',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetBetweenDatesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_between_dates(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_between_dates_mapped_args(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_between_dates_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_between_dates(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_between_dates_mapped_args(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_between_dates_oapg(
            query_params=args.query,
        )

class GetBetweenDates(BaseApi):

    async def aget_between_dates(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> APITimesheetEntryPagedResponsePydantic:
        raw_response = await self.raw.aget_between_dates(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return APITimesheetEntryPagedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(APITimesheetEntryPagedResponsePydantic, raw_response.body)
    
    
    def get_between_dates(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> APITimesheetEntryPagedResponsePydantic:
        raw_response = self.raw.get_between_dates(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
        )
        if validate:
            return APITimesheetEntryPagedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(APITimesheetEntryPagedResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_between_dates_mapped_args(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_between_dates_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        _from: typing.Optional[datetime] = None,
        to: typing.Optional[datetime] = None,
        employee_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        task_ids: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_between_dates_mapped_args(
            _from=_from,
            to=to,
            employee_ids=employee_ids,
            project_ids=project_ids,
            task_ids=task_ids,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_between_dates_oapg(
            query_params=args.query,
        )

