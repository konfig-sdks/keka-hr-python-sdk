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

from keka_hr_python_sdk.model.goal_status import GoalStatus as GoalStatusSchema
from keka_hr_python_sdk.model.api_update_goal_progress import APIUpdateGoalProgress as APIUpdateGoalProgressSchema
from keka_hr_python_sdk.model.boolean_response import BooleanResponse as BooleanResponseSchema

from keka_hr_python_sdk.type.api_update_goal_progress import APIUpdateGoalProgress
from keka_hr_python_sdk.type.goal_status import GoalStatus
from keka_hr_python_sdk.type.boolean_response import BooleanResponse

from ...api_client import Dictionary
from keka_hr_python_sdk.pydantic.api_update_goal_progress import APIUpdateGoalProgress as APIUpdateGoalProgressPydantic
from keka_hr_python_sdk.pydantic.goal_status import GoalStatus as GoalStatusPydantic
from keka_hr_python_sdk.pydantic.boolean_response import BooleanResponse as BooleanResponsePydantic

# Path params
GoalIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'goalId': typing.Union[GoalIdSchema, str, ],
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


request_path_goal_id = api_client.PathParameter(
    name="goalId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GoalIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = APIUpdateGoalProgressSchema
SchemaForRequestBodyTextJson = APIUpdateGoalProgressSchema
SchemaForRequestBodyApplicationJsonPatchjson = APIUpdateGoalProgressSchema
SchemaForRequestBodyApplicationJson = APIUpdateGoalProgressSchema


request_body_api_update_goal_progress = api_client.RequestBody(
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
)
SchemaFor200ResponseBodyApplicationJson = BooleanResponseSchema
SchemaFor200ResponseBodyTextJson = BooleanResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BooleanResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BooleanResponse


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
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _update_progress_mapped_args(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if current_value is not None:
            _body["currentValue"] = current_value
        if status is not None:
            _body["status"] = status
        if updated_by is not None:
            _body["updatedBy"] = updated_by
        if note is not None:
            _body["note"] = note
        args.body = _body
        if goal_id is not None:
            _path_params["goalId"] = goal_id
        args.path = _path_params
        return args

    async def _aupdate_progress_oapg(
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
        Update goal progress
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_goal_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/pms/goals/{goalId}/progress',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_api_update_goal_progress.serialize(body, content_type)
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


    def _update_progress_oapg(
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
        Update goal progress
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_goal_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/pms/goals/{goalId}/progress',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_api_update_goal_progress.serialize(body, content_type)
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


class UpdateProgressRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_progress(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_progress_mapped_args(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
        )
        return await self._aupdate_progress_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_progress(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_progress_mapped_args(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
        )
        return self._update_progress_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateProgress(BaseApi):

    async def aupdate_progress(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> BooleanResponsePydantic:
        raw_response = await self.raw.aupdate_progress(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
            **kwargs,
        )
        if validate:
            return BooleanResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BooleanResponsePydantic, raw_response.body)
    
    
    def update_progress(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> BooleanResponsePydantic:
        raw_response = self.raw.update_progress(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
        )
        if validate:
            return BooleanResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BooleanResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_progress_mapped_args(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
        )
        return await self._aupdate_progress_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        current_value: typing.Union[int, float],
        status: GoalStatus,
        updated_by: str,
        goal_id: str,
        note: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_progress_mapped_args(
            current_value=current_value,
            status=status,
            updated_by=updated_by,
            goal_id=goal_id,
            note=note,
        )
        return self._update_progress_oapg(
            body=args.body,
            path_params=args.path,
        )

