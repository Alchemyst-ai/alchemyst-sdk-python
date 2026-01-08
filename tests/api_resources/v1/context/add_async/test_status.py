# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alchemyst_ai import AlchemystAI, AsyncAlchemystAI
from alchemyst_ai.types.v1.context.add_async import StatusListResponse, StatusRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlchemystAI) -> None:
        status = client.v1.context.add_async.status.retrieve(
            "id",
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlchemystAI) -> None:
        response = client.v1.context.add_async.status.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlchemystAI) -> None:
        with client.v1.context.add_async.status.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusRetrieveResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: AlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.context.add_async.status.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: AlchemystAI) -> None:
        status = client.v1.context.add_async.status.list()
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: AlchemystAI) -> None:
        status = client.v1.context.add_async.status.list(
            limit="limit",
            offset="offset",
            type="all",
        )
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlchemystAI) -> None:
        response = client.v1.context.add_async.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlchemystAI) -> None:
        with client.v1.context.add_async.status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusListResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlchemystAI) -> None:
        status = await async_client.v1.context.add_async.status.retrieve(
            "id",
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.add_async.status.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.add_async.status.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusRetrieveResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.context.add_async.status.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlchemystAI) -> None:
        status = await async_client.v1.context.add_async.status.list()
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        status = await async_client.v1.context.add_async.status.list(
            limit="limit",
            offset="offset",
            type="all",
        )
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.add_async.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusListResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.add_async.status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusListResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True
