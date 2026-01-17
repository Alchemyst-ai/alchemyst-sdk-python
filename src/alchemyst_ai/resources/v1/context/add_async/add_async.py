# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.context import add_async_create_params
from .....types.v1.context.add_async_cancel_response import AddAsyncCancelResponse
from .....types.v1.context.add_async_create_response import AddAsyncCreateResponse

__all__ = ["AddAsyncResource", "AsyncAddAsyncResource"]


class AddAsyncResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AddAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AddAsyncResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        context_type: Literal["resource", "conversation", "instruction"],
        documents: Iterable[add_async_create_params.Document],
        scope: Literal["internal", "external"],
        source: str,
        metadata: add_async_create_params.Metadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddAsyncCreateResponse:
        """
        This endpoint accepts context data and queues it for asynchronous processing by
        the context processor. It returns a success or error response depending on the
        queuing result.

        Args:
          context_type: Type of context being added

          documents: Array of documents with content and additional metadata

          scope: Scope of the context

          source: The source of the context data

          metadata: Additional metadata for the context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/add-async",
            body=maybe_transform(
                {
                    "context_type": context_type,
                    "documents": documents,
                    "scope": scope,
                    "source": source,
                    "metadata": metadata,
                },
                add_async_create_params.AddAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddAsyncCreateResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddAsyncCancelResponse:
        """
        Attempts to cancel a context add job by job id.

        - If the job is already completed or failed, returns 404.
        - If the job is currently running ("active"), returns 409 and cannot be
          cancelled.
        - Only jobs in "waiting" or "delayed" state can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/context/add-async/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddAsyncCancelResponse,
        )


class AsyncAddAsyncResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AsyncAddAsyncResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        context_type: Literal["resource", "conversation", "instruction"],
        documents: Iterable[add_async_create_params.Document],
        scope: Literal["internal", "external"],
        source: str,
        metadata: add_async_create_params.Metadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddAsyncCreateResponse:
        """
        This endpoint accepts context data and queues it for asynchronous processing by
        the context processor. It returns a success or error response depending on the
        queuing result.

        Args:
          context_type: Type of context being added

          documents: Array of documents with content and additional metadata

          scope: Scope of the context

          source: The source of the context data

          metadata: Additional metadata for the context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/add-async",
            body=await async_maybe_transform(
                {
                    "context_type": context_type,
                    "documents": documents,
                    "scope": scope,
                    "source": source,
                    "metadata": metadata,
                },
                add_async_create_params.AddAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddAsyncCreateResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddAsyncCancelResponse:
        """
        Attempts to cancel a context add job by job id.

        - If the job is already completed or failed, returns 404.
        - If the job is currently running ("active"), returns 409 and cannot be
          cancelled.
        - Only jobs in "waiting" or "delayed" state can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/context/add-async/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddAsyncCancelResponse,
        )


class AddAsyncResourceWithRawResponse:
    def __init__(self, add_async: AddAsyncResource) -> None:
        self._add_async = add_async

        self.create = to_raw_response_wrapper(
            add_async.create,
        )
        self.cancel = to_raw_response_wrapper(
            add_async.cancel,
        )

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._add_async.status)


class AsyncAddAsyncResourceWithRawResponse:
    def __init__(self, add_async: AsyncAddAsyncResource) -> None:
        self._add_async = add_async

        self.create = async_to_raw_response_wrapper(
            add_async.create,
        )
        self.cancel = async_to_raw_response_wrapper(
            add_async.cancel,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._add_async.status)


class AddAsyncResourceWithStreamingResponse:
    def __init__(self, add_async: AddAsyncResource) -> None:
        self._add_async = add_async

        self.create = to_streamed_response_wrapper(
            add_async.create,
        )
        self.cancel = to_streamed_response_wrapper(
            add_async.cancel,
        )

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._add_async.status)


class AsyncAddAsyncResourceWithStreamingResponse:
    def __init__(self, add_async: AsyncAddAsyncResource) -> None:
        self._add_async = add_async

        self.create = async_to_streamed_response_wrapper(
            add_async.create,
        )
        self.cancel = async_to_streamed_response_wrapper(
            add_async.cancel,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._add_async.status)
