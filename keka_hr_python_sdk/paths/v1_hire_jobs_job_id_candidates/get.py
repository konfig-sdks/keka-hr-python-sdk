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

from keka_hr_python_sdk.model.jobs_get_candidates_response import JobsGetCandidatesResponse as JobsGetCandidatesResponseSchema
from keka_hr_python_sdk.model.jobs_get_candidates200_response import JobsGetCandidates200Response as JobsGetCandidates200ResponseSchema

from keka_hr_python_sdk.type.jobs_get_candidates_response import JobsGetCandidatesResponse
from keka_hr_python_sdk.type.jobs_get_candidates200_response import JobsGetCandidates200Response

from ...api_client import Dictionary
from keka_hr_python_sdk.pydantic.jobs_get_candidates_response import JobsGetCandidatesResponse as JobsGetCandidatesResponsePydantic
from keka_hr_python_sdk.pydantic.jobs_get_candidates200_response import JobsGetCandidates200Response as JobsGetCandidates200ResponsePydantic

from . import path

# Query params
IsArchivedSchema = schemas.BoolSchema
LastModifiedSchema = schemas.DateTimeSchema
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
        'isArchived': typing.Union[IsArchivedSchema, bool, ],
        'lastModified': typing.Union[LastModifiedSchema, str, datetime, ],
        'pageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_is_archived = api_client.QueryParameter(
    name="isArchived",
    style=api_client.ParameterStyle.FORM,
    schema=IsArchivedSchema,
    explode=True,
)
request_query_last_modified = api_client.QueryParameter(
    name="lastModified",
    style=api_client.ParameterStyle.FORM,
    schema=LastModifiedSchema,
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
# Path params
JobIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'jobId': typing.Union[JobIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_job_id = api_client.PathParameter(
    name="jobId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=JobIdSchema,
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = JobsGetCandidatesResponseSchema
SchemaFor200ResponseBodyTextJson = JobsGetCandidates200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: JobsGetCandidatesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: JobsGetCandidatesResponse


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


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _get_candidates_mapped_args(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if is_archived is not None:
            _query_params["isArchived"] = is_archived
        if last_modified is not None:
            _query_params["lastModified"] = last_modified
        if page_number is not None:
            _query_params["pageNumber"] = page_number
        if page_size is not None:
            _query_params["pageSize"] = page_size
        if job_id is not None:
            _path_params["jobId"] = job_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_candidates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Get job candidates
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_job_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_is_archived,
            request_query_last_modified,
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
            path_template='/v1/hire/jobs/{jobId}/candidates',
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


    def _get_candidates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get job candidates
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_job_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_is_archived,
            request_query_last_modified,
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
            path_template='/v1/hire/jobs/{jobId}/candidates',
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


class GetCandidatesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_candidates(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_candidates_mapped_args(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_candidates_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_candidates(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_candidates_mapped_args(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_candidates_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetCandidates(BaseApi):

    async def aget_candidates(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> JobsGetCandidatesResponsePydantic:
        raw_response = await self.raw.aget_candidates(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return RootModel[JobsGetCandidatesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(JobsGetCandidatesResponsePydantic, raw_response.body)
    
    
    def get_candidates(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> JobsGetCandidatesResponsePydantic:
        raw_response = self.raw.get_candidates(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
        )
        if validate:
            return RootModel[JobsGetCandidatesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(JobsGetCandidatesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_candidates_mapped_args(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
        )
        return await self._aget_candidates_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        job_id: str,
        is_archived: typing.Optional[bool] = None,
        last_modified: typing.Optional[datetime] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_candidates_mapped_args(
            job_id=job_id,
            is_archived=is_archived,
            last_modified=last_modified,
            page_number=page_number,
            page_size=page_size,
        )
        return self._get_candidates_oapg(
            query_params=args.query,
            path_params=args.path,
        )

