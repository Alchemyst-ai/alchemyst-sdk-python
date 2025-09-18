# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ....types.v1.org import context_view_params
from ....types.v1.org.context_view_response import ContextViewResponse

__all__ = ["ContextResource", "AsyncContextResource"]


class ContextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return ContextResourceWithStreamingResponse(self)

    def view(
        self,
        *,
        user_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextViewResponse:
        """
        View organization context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/org/context/view",
            body=maybe_transform({"user_ids": user_ids}, context_view_params.ContextViewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextViewResponse,
        )


class AsyncContextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AsyncContextResourceWithStreamingResponse(self)

    async def view(
        self,
        *,
        user_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextViewResponse:
        """
        View organization context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/org/context/view",
            body=await async_maybe_transform({"user_ids": user_ids}, context_view_params.ContextViewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextViewResponse,
        )


class ContextResourceWithRawResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.view = to_raw_response_wrapper(
            context.view,
        )


class AsyncContextResourceWithRawResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.view = async_to_raw_response_wrapper(
            context.view,
        )


class ContextResourceWithStreamingResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.view = to_streamed_response_wrapper(
            context.view,
        )


class AsyncContextResourceWithStreamingResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.view = async_to_streamed_response_wrapper(
            context.view,
        )
