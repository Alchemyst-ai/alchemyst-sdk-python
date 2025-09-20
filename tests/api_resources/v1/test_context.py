# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alchemyst_ai import AlchemystAI, AsyncAlchemystAI
from alchemyst_ai.types.v1 import (
    ContextSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlchemystAI) -> None:
        context = client.v1.context.delete()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: AlchemystAI) -> None:
        context = client.v1.context.delete(
            by_doc=True,
            by_id=True,
            organization_id="organization_id",
            source="source",
            user_id="user_id",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlchemystAI) -> None:
        response = client.v1.context.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlchemystAI) -> None:
        with client.v1.context.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: AlchemystAI) -> None:
        context = client.v1.context.add()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: AlchemystAI) -> None:
        context = client.v1.context.add(
            context_type="resource",
            documents=[{"content": "content"}],
            metadata={
                "file_name": "fileName",
                "file_size": 0,
                "file_type": "fileType",
                "last_modified": "lastModified",
            },
            scope="internal",
            source="source",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: AlchemystAI) -> None:
        response = client.v1.context.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: AlchemystAI) -> None:
        with client.v1.context.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: AlchemystAI) -> None:
        context = client.v1.context.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        )
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: AlchemystAI) -> None:
        context = client.v1.context.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
            metadata={},
            scope="internal",
            user_id="user123",
        )
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: AlchemystAI) -> None:
        response = client.v1.context.with_raw_response.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: AlchemystAI) -> None:
        with client.v1.context.with_streaming_response.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextSearchResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.delete()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.delete(
            by_doc=True,
            by_id=True,
            organization_id="organization_id",
            source="source",
            user_id="user_id",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.add()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.add(
            context_type="resource",
            documents=[{"content": "content"}],
            metadata={
                "file_name": "fileName",
                "file_size": 0,
                "file_type": "fileType",
                "last_modified": "lastModified",
            },
            scope="internal",
            source="source",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.with_raw_response.add()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.with_streaming_response.add() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        )
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        context = await async_client.v1.context.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
            metadata={},
            scope="internal",
            user_id="user123",
        )
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.with_raw_response.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextSearchResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.with_streaming_response.search(
            minimum_similarity_threshold=0.5,
            query="search query for user preferences",
            similarity_threshold=0.8,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextSearchResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True
