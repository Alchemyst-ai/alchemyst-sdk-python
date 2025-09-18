# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alchemyst_ai import AlchemystAI, AsyncAlchemystAI
from alchemyst_ai.types.v1.org import ContextViewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_view(self, client: AlchemystAI) -> None:
        context = client.v1.org.context.view(
            user_ids=["string"],
        )
        assert_matches_type(ContextViewResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_view(self, client: AlchemystAI) -> None:
        response = client.v1.org.context.with_raw_response.view(
            user_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextViewResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_view(self, client: AlchemystAI) -> None:
        with client.v1.org.context.with_streaming_response.view(
            user_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextViewResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_view(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.org.context.view(
            user_ids=["string"],
        )
        assert_matches_type(ContextViewResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_view(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.org.context.with_raw_response.view(
            user_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextViewResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.org.context.with_streaming_response.view(
            user_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextViewResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True
