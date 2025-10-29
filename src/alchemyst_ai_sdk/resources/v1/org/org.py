# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def context(self) -> ContextResource:
        return ContextResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def context(self) -> AsyncContextResource:
        return AsyncContextResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Alchemyst-ai/alchemyst-sdk-python#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        return ContextResourceWithRawResponse(self._org.context)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        return AsyncContextResourceWithRawResponse(self._org.context)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        return ContextResourceWithStreamingResponse(self._org.context)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        return AsyncContextResourceWithStreamingResponse(self._org.context)
