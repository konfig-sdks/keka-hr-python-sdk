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

from keka_hr_python_sdk.model.jobs_update_candidate_request3 import JobsUpdateCandidateRequest3 as JobsUpdateCandidateRequest3Schema
from keka_hr_python_sdk.model.ok_error_response import OkErrorResponse as OkErrorResponseSchema
from keka_hr_python_sdk.model.jobs_update_candidate_request import JobsUpdateCandidateRequest as JobsUpdateCandidateRequestSchema
from keka_hr_python_sdk.model.jobs_update_candidate_request1 import JobsUpdateCandidateRequest1 as JobsUpdateCandidateRequest1Schema
from keka_hr_python_sdk.model.jobs_update_candidate_request2 import JobsUpdateCandidateRequest2 as JobsUpdateCandidateRequest2Schema

from keka_hr_python_sdk.type.ok_error_response import OkErrorResponse
from keka_hr_python_sdk.type.jobs_update_candidate_request import JobsUpdateCandidateRequest
from keka_hr_python_sdk.type.jobs_update_candidate_request1 import JobsUpdateCandidateRequest1
from keka_hr_python_sdk.type.jobs_update_candidate_request2 import JobsUpdateCandidateRequest2
from keka_hr_python_sdk.type.jobs_update_candidate_request3 import JobsUpdateCandidateRequest3

from ...api_client import Dictionary
from keka_hr_python_sdk.pydantic.ok_error_response import OkErrorResponse as OkErrorResponsePydantic
from keka_hr_python_sdk.pydantic.jobs_update_candidate_request2 import JobsUpdateCandidateRequest2 as JobsUpdateCandidateRequest2Pydantic
from keka_hr_python_sdk.pydantic.jobs_update_candidate_request3 import JobsUpdateCandidateRequest3 as JobsUpdateCandidateRequest3Pydantic
from keka_hr_python_sdk.pydantic.jobs_update_candidate_request1 import JobsUpdateCandidateRequest1 as JobsUpdateCandidateRequest1Pydantic
from keka_hr_python_sdk.pydantic.jobs_update_candidate_request import JobsUpdateCandidateRequest as JobsUpdateCandidateRequestPydantic

from . import path

# Path params
CandidateIdSchema = schemas.StrSchema
JobIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'candidateId': typing.Union[CandidateIdSchema, str, ],
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


request_path_candidate_id = api_client.PathParameter(
    name="candidateId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CandidateIdSchema,
    required=True,
)
request_path_job_id = api_client.PathParameter(
    name="jobId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=JobIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = JobsUpdateCandidateRequest1Schema
SchemaForRequestBodyTextJson = JobsUpdateCandidateRequest2Schema
SchemaForRequestBodyApplicationJsonPatchjson = JobsUpdateCandidateRequestSchema
SchemaForRequestBodyApplicationJson = JobsUpdateCandidateRequest3Schema


request_body_jobs_update_candidate_request1 = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = schemas.StrSchema
SchemaFor200ResponseBodyTextJson = schemas.StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: str


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
SchemaFor400ResponseBodyApplicationJson = OkErrorResponseSchema
SchemaFor400ResponseBodyTextJson = OkErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OkErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OkErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
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
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _update_candidate_mapped_args(
        self,
        candidate_id: str,
        job_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        args.body = _body
        if candidate_id is not None:
            _path_params["candidateId"] = candidate_id
        if job_id is not None:
            _path_params["jobId"] = job_id
        args.path = _path_params
        return args

    async def _aupdate_candidate_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Updated a candidate
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_candidate_id,
            request_path_job_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/hire/jobs/{jobId}/candidate/{candidateId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_jobs_update_candidate_request1.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_candidate_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Updated a candidate
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_candidate_id,
            request_path_job_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/hire/jobs/{jobId}/candidate/{candidateId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_jobs_update_candidate_request1.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateCandidateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_candidate(
        self,
        candidate_id: str,
        job_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_candidate_mapped_args(
            candidate_id=candidate_id,
            job_id=job_id,
        )
        return await self._aupdate_candidate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_candidate(
        self,
        candidate_id: str,
        job_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_candidate_mapped_args(
            candidate_id=candidate_id,
            job_id=job_id,
        )
        return self._update_candidate_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateCandidate(BaseApi):

    async def aupdate_candidate(
        self,
        candidate_id: str,
        job_id: str,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.aupdate_candidate(
            candidate_id=candidate_id,
            job_id=job_id,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def update_candidate(
        self,
        candidate_id: str,
        job_id: str,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.update_candidate(
            candidate_id=candidate_id,
            job_id=job_id,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        candidate_id: str,
        job_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_candidate_mapped_args(
            candidate_id=candidate_id,
            job_id=job_id,
        )
        return await self._aupdate_candidate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        candidate_id: str,
        job_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_candidate_mapped_args(
            candidate_id=candidate_id,
            job_id=job_id,
        )
        return self._update_candidate_oapg(
            body=args.body,
            path_params=args.path,
        )

