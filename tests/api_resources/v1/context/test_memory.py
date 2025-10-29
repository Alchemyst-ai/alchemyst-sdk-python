# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from alchemyst_ai import AlchemystAI, AsyncAlchemystAI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlchemystAI) -> None:
        memory = client.v1.context.memory.delete()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: AlchemystAI) -> None:
        memory = client.v1.context.memory.delete(
            memory_id="memoryId",
            organization_id="organization_id",
            user_id="user_id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlchemystAI) -> None:
        response = client.v1.context.memory.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlchemystAI) -> None:
        with client.v1.context.memory.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: AlchemystAI) -> None:
        memory = client.v1.context.memory.add()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: AlchemystAI) -> None:
        memory = client.v1.context.memory.add(
            contents=[{"content": "content"}],
            memory_id="memoryId",
        )
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: AlchemystAI) -> None:
        response = client.v1.context.memory.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: AlchemystAI) -> None:
        with client.v1.context.memory.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlchemystAI) -> None:
        memory = await async_client.v1.context.memory.delete()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        memory = await async_client.v1.context.memory.delete(
            memory_id="memoryId",
            organization_id="organization_id",
            user_id="user_id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.memory.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.memory.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncAlchemystAI) -> None:
        memory = await async_client.v1.context.memory.add()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        memory = await async_client.v1.context.memory.add(
            contents=[{"content": "content"}],
            memory_id="memoryId",
        )
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.memory.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.memory.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True
