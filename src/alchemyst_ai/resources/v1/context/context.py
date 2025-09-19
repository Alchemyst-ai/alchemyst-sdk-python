# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .view import (
    ViewResource,
    AsyncViewResource,
    ViewResourceWithRawResponse,
    AsyncViewResourceWithRawResponse,
    ViewResourceWithStreamingResponse,
    AsyncViewResourceWithStreamingResponse,
)
from .traces import (
    TracesResource,
    AsyncTracesResource,
    TracesResourceWithRawResponse,
    AsyncTracesResourceWithRawResponse,
    TracesResourceWithStreamingResponse,
    AsyncTracesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import context_add_params, context_delete_params, context_search_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.context_search_response import ContextSearchResponse

__all__ = ["ContextResource", "AsyncContextResource"]


class ContextResource(SyncAPIResource):
    @cached_property
    def traces(self) -> TracesResource:
        return TracesResource(self._client)

    @cached_property
    def view(self) -> ViewResource:
        return ViewResource(self._client)

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

    def delete(
        self,
        *,
        by_doc: Optional[bool] | Omit = omit,
        by_id: Optional[bool] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        source: str | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes context data based on provided parameters

        Args:
          by_doc: Flag to delete by document

          by_id: Flag to delete by ID

          organization_id: Optional organization ID

          source: Source identifier for the context

          user_id: Optional user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/delete",
            body=maybe_transform(
                {
                    "by_doc": by_doc,
                    "by_id": by_id,
                    "organization_id": organization_id,
                    "source": source,
                    "user_id": user_id,
                },
                context_delete_params.ContextDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        *,
        context_type: Literal["resource", "conversation", "instruction"] | Omit = omit,
        documents: Iterable[context_add_params.Document] | Omit = omit,
        metadata: context_add_params.Metadata | Omit = omit,
        scope: Literal["internal", "external"] | Omit = omit,
        source: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This endpoint accepts context data and sends it to a context processor for
        further handling. It returns a success or error response depending on the result
        from the context processor.

        Args:
          context_type: Type of context being added

          documents: Array of documents with content and additional metadata

          metadata: Additional metadata for the context

          scope: Scope of the context

          source: The source of the context data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/add",
            body=maybe_transform(
                {
                    "context_type": context_type,
                    "documents": documents,
                    "metadata": metadata,
                    "scope": scope,
                    "source": source,
                },
                context_add_params.ContextAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def search(
        self,
        *,
        minimum_similarity_threshold: float,
        query: str,
        similarity_threshold: float,
        metadata: object | Omit = omit,
        scope: Literal["internal", "external"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextSearchResponse:
        """
        This endpoint sends a search request to the context processor to retrieve
        relevant context data based on the provided query.

        Args:
          minimum_similarity_threshold: Minimum similarity threshold

          query: The search query used to search for context data

          similarity_threshold: Maximum similarity threshold (must be >= minimum_similarity_threshold)

          metadata: Additional metadata for the search

          scope: Search scope

          user_id: The ID of the user making the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/context/search",
            body=maybe_transform(
                {
                    "minimum_similarity_threshold": minimum_similarity_threshold,
                    "query": query,
                    "similarity_threshold": similarity_threshold,
                    "metadata": metadata,
                    "scope": scope,
                    "user_id": user_id,
                },
                context_search_params.ContextSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSearchResponse,
        )


class AsyncContextResource(AsyncAPIResource):
    @cached_property
    def traces(self) -> AsyncTracesResource:
        return AsyncTracesResource(self._client)

    @cached_property
    def view(self) -> AsyncViewResource:
        return AsyncViewResource(self._client)

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

    async def delete(
        self,
        *,
        by_doc: Optional[bool] | Omit = omit,
        by_id: Optional[bool] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        source: str | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes context data based on provided parameters

        Args:
          by_doc: Flag to delete by document

          by_id: Flag to delete by ID

          organization_id: Optional organization ID

          source: Source identifier for the context

          user_id: Optional user ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/delete",
            body=await async_maybe_transform(
                {
                    "by_doc": by_doc,
                    "by_id": by_id,
                    "organization_id": organization_id,
                    "source": source,
                    "user_id": user_id,
                },
                context_delete_params.ContextDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        *,
        context_type: Literal["resource", "conversation", "instruction"] | Omit = omit,
        documents: Iterable[context_add_params.Document] | Omit = omit,
        metadata: context_add_params.Metadata | Omit = omit,
        scope: Literal["internal", "external"] | Omit = omit,
        source: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This endpoint accepts context data and sends it to a context processor for
        further handling. It returns a success or error response depending on the result
        from the context processor.

        Args:
          context_type: Type of context being added

          documents: Array of documents with content and additional metadata

          metadata: Additional metadata for the context

          scope: Scope of the context

          source: The source of the context data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/add",
            body=await async_maybe_transform(
                {
                    "context_type": context_type,
                    "documents": documents,
                    "metadata": metadata,
                    "scope": scope,
                    "source": source,
                },
                context_add_params.ContextAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def search(
        self,
        *,
        minimum_similarity_threshold: float,
        query: str,
        similarity_threshold: float,
        metadata: object | Omit = omit,
        scope: Literal["internal", "external"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextSearchResponse:
        """
        This endpoint sends a search request to the context processor to retrieve
        relevant context data based on the provided query.

        Args:
          minimum_similarity_threshold: Minimum similarity threshold

          query: The search query used to search for context data

          similarity_threshold: Maximum similarity threshold (must be >= minimum_similarity_threshold)

          metadata: Additional metadata for the search

          scope: Search scope

          user_id: The ID of the user making the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/context/search",
            body=await async_maybe_transform(
                {
                    "minimum_similarity_threshold": minimum_similarity_threshold,
                    "query": query,
                    "similarity_threshold": similarity_threshold,
                    "metadata": metadata,
                    "scope": scope,
                    "user_id": user_id,
                },
                context_search_params.ContextSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSearchResponse,
        )


class ContextResourceWithRawResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.delete = to_raw_response_wrapper(
            context.delete,
        )
        self.add = to_raw_response_wrapper(
            context.add,
        )
        self.search = to_raw_response_wrapper(
            context.search,
        )

    @cached_property
    def traces(self) -> TracesResourceWithRawResponse:
        return TracesResourceWithRawResponse(self._context.traces)

    @cached_property
    def view(self) -> ViewResourceWithRawResponse:
        return ViewResourceWithRawResponse(self._context.view)


class AsyncContextResourceWithRawResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.delete = async_to_raw_response_wrapper(
            context.delete,
        )
        self.add = async_to_raw_response_wrapper(
            context.add,
        )
        self.search = async_to_raw_response_wrapper(
            context.search,
        )

    @cached_property
    def traces(self) -> AsyncTracesResourceWithRawResponse:
        return AsyncTracesResourceWithRawResponse(self._context.traces)

    @cached_property
    def view(self) -> AsyncViewResourceWithRawResponse:
        return AsyncViewResourceWithRawResponse(self._context.view)


class ContextResourceWithStreamingResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.delete = to_streamed_response_wrapper(
            context.delete,
        )
        self.add = to_streamed_response_wrapper(
            context.add,
        )
        self.search = to_streamed_response_wrapper(
            context.search,
        )

    @cached_property
    def traces(self) -> TracesResourceWithStreamingResponse:
        return TracesResourceWithStreamingResponse(self._context.traces)

    @cached_property
    def view(self) -> ViewResourceWithStreamingResponse:
        return ViewResourceWithStreamingResponse(self._context.view)


class AsyncContextResourceWithStreamingResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.delete = async_to_streamed_response_wrapper(
            context.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            context.add,
        )
        self.search = async_to_streamed_response_wrapper(
            context.search,
        )

    @cached_property
    def traces(self) -> AsyncTracesResourceWithStreamingResponse:
        return AsyncTracesResourceWithStreamingResponse(self._context.traces)

    @cached_property
    def view(self) -> AsyncViewResourceWithStreamingResponse:
        return AsyncViewResourceWithStreamingResponse(self._context.view)
