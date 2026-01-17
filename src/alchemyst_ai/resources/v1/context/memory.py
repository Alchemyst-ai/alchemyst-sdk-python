# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.context import memory_add_params, memory_delete_params, memory_update_params
from ....types.v1.context.memory_add_response import MemoryAddResponse
from ....types.v1.context.memory_update_response import MemoryUpdateResponse

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        contents: Iterable[memory_update_params.Content],
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryUpdateResponse:
        """
        This endpoint updates memory context data.

        Args:
          contents: Array of updated content objects

          session_id: The ID of the memory to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/memory/update",
            body=maybe_transform(
                {
                    "contents": contents,
                    "session_id": session_id,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    def delete(
        self,
        *,
        memory_id: str,
        organization_id: Optional[str],
        by_doc: Optional[bool] | Omit = omit,
        by_id: Optional[bool] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes memory context data based on provided parameters.

        Args:
          memory_id: The ID of the memory to delete

          organization_id: Organization ID

          by_doc: Delete by document flag

          by_id: Delete by ID flag

          user_id: Optional user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v1/context/memory/delete",
            body=maybe_transform(
                {
                    "memory_id": memory_id,
                    "organization_id": organization_id,
                    "by_doc": by_doc,
                    "by_id": by_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add(
        self,
        *,
        contents: Iterable[memory_add_params.Content],
        session_id: str,
        metadata: memory_add_params.Metadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAddResponse:
        """
        This endpoint adds memory (chat history) as context.

        Args:
          contents: Array of content objects. Each object must contain at least the 'content' field.
              Additional properties are allowed.

          session_id: The ID of the session

          metadata: Optional metadata for the memory context. Defaults to ["default"] if not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/memory/add",
            body=maybe_transform(
                {
                    "contents": contents,
                    "session_id": session_id,
                    "metadata": metadata,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryAddResponse,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        contents: Iterable[memory_update_params.Content],
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryUpdateResponse:
        """
        This endpoint updates memory context data.

        Args:
          contents: Array of updated content objects

          session_id: The ID of the memory to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/memory/update",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "session_id": session_id,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    async def delete(
        self,
        *,
        memory_id: str,
        organization_id: Optional[str],
        by_doc: Optional[bool] | Omit = omit,
        by_id: Optional[bool] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes memory context data based on provided parameters.

        Args:
          memory_id: The ID of the memory to delete

          organization_id: Organization ID

          by_doc: Delete by document flag

          by_id: Delete by ID flag

          user_id: Optional user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v1/context/memory/delete",
            body=await async_maybe_transform(
                {
                    "memory_id": memory_id,
                    "organization_id": organization_id,
                    "by_doc": by_doc,
                    "by_id": by_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add(
        self,
        *,
        contents: Iterable[memory_add_params.Content],
        session_id: str,
        metadata: memory_add_params.Metadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAddResponse:
        """
        This endpoint adds memory (chat history) as context.

        Args:
          contents: Array of content objects. Each object must contain at least the 'content' field.
              Additional properties are allowed.

          session_id: The ID of the session

          metadata: Optional metadata for the memory context. Defaults to ["default"] if not
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/memory/add",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "session_id": session_id,
                    "metadata": metadata,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryAddResponse,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_raw_response_wrapper(
            memory.update,
        )
        self.delete = to_raw_response_wrapper(
            memory.delete,
        )
        self.add = to_raw_response_wrapper(
            memory.add,
        )


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_raw_response_wrapper(
            memory.update,
        )
        self.delete = async_to_raw_response_wrapper(
            memory.delete,
        )
        self.add = async_to_raw_response_wrapper(
            memory.add,
        )


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = to_streamed_response_wrapper(
            memory.add,
        )


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            memory.add,
        )
