# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alchemyst_ai import AlchemystAI, AsyncAlchemystAI
from alchemyst_ai.types.v1.context import TraceListResponse, TraceDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: AlchemystAI) -> None:
        trace = client.v1.context.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlchemystAI) -> None:
        response = client.v1.context.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlchemystAI) -> None:
        with client.v1.context.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlchemystAI) -> None:
        trace = client.v1.context.traces.delete(
            "traceId",
        )
        assert_matches_type(TraceDeleteResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlchemystAI) -> None:
        response = client.v1.context.traces.with_raw_response.delete(
            "traceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(TraceDeleteResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlchemystAI) -> None:
        with client.v1.context.traces.with_streaming_response.delete(
            "traceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(TraceDeleteResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            client.v1.context.traces.with_raw_response.delete(
                "",
            )


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlchemystAI) -> None:
        trace = await async_client.v1.context.traces.list()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.traces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceListResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.traces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceListResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlchemystAI) -> None:
        trace = await async_client.v1.context.traces.delete(
            "traceId",
        )
        assert_matches_type(TraceDeleteResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.traces.with_raw_response.delete(
            "traceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(TraceDeleteResponse, trace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.traces.with_streaming_response.delete(
            "traceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(TraceDeleteResponse, trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trace_id` but received ''"):
            await async_client.v1.context.traces.with_raw_response.delete(
                "",
            )
