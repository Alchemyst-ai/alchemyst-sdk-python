# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.v1.context import view_retrieve_params
from ....types.v1.context.view_retrieve_response import ViewRetrieveResponse

__all__ = ["ViewResource", "AsyncViewResource"]


class ViewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return ViewResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        file_name: str | Omit = omit,
        magic_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewRetrieveResponse:
        """
        Gets the context information for the authenticated user

        Args:
          file_name: Name of the file to retrieve context for

          magic_key: Magic key for context retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/context/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_name": file_name,
                        "magic_key": magic_key,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
            ),
            cast_to=ViewRetrieveResponse,
        )

    def docs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Fetches documents view for authenticated user with optional organization context
        """
        return self._get(
            "/api/v1/context/view/docs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncViewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AsyncViewResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        file_name: str | Omit = omit,
        magic_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewRetrieveResponse:
        """
        Gets the context information for the authenticated user

        Args:
          file_name: Name of the file to retrieve context for

          magic_key: Magic key for context retrieval

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/context/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "file_name": file_name,
                        "magic_key": magic_key,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
            ),
            cast_to=ViewRetrieveResponse,
        )

    async def docs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Fetches documents view for authenticated user with optional organization context
        """
        return await self._get(
            "/api/v1/context/view/docs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ViewResourceWithRawResponse:
    def __init__(self, view: ViewResource) -> None:
        self._view = view

        self.retrieve = to_raw_response_wrapper(
            view.retrieve,
        )
        self.docs = to_raw_response_wrapper(
            view.docs,
        )


class AsyncViewResourceWithRawResponse:
    def __init__(self, view: AsyncViewResource) -> None:
        self._view = view

        self.retrieve = async_to_raw_response_wrapper(
            view.retrieve,
        )
        self.docs = async_to_raw_response_wrapper(
            view.docs,
        )


class ViewResourceWithStreamingResponse:
    def __init__(self, view: ViewResource) -> None:
        self._view = view

        self.retrieve = to_streamed_response_wrapper(
            view.retrieve,
        )
        self.docs = to_streamed_response_wrapper(
            view.docs,
        )


class AsyncViewResourceWithStreamingResponse:
    def __init__(self, view: AsyncViewResource) -> None:
        self._view = view

        self.retrieve = async_to_streamed_response_wrapper(
            view.retrieve,
        )
        self.docs = async_to_streamed_response_wrapper(
            view.docs,
        )
