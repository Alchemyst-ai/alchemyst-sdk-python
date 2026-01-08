# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alchemyst_ai import AlchemystAI, AsyncAlchemystAI
from alchemyst_ai.types.v1.context import AddAsyncCancelResponse, AddAsyncCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddAsync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: AlchemystAI) -> None:
        add_async = client.v1.context.add_async.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        )
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: AlchemystAI) -> None:
        add_async = client.v1.context.add_async.create(
            context_type="resource",
            documents=[{"content": "Customer asked about pricing for the Scale plan."}],
            scope="internal",
            source="support-inbox",
            metadata={
                "file_name": "support_thread_TCK-1234.txt",
                "file_size": 2048,
                "file_type": "text/plain",
                "group_name": ["support", "pricing"],
                "last_modified": "2025-01-10T12:34:56.000Z",
            },
        )
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlchemystAI) -> None:
        response = client.v1.context.add_async.with_raw_response.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add_async = response.parse()
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlchemystAI) -> None:
        with client.v1.context.add_async.with_streaming_response.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add_async = response.parse()
            assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: AlchemystAI) -> None:
        add_async = client.v1.context.add_async.cancel(
            "id",
        )
        assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: AlchemystAI) -> None:
        response = client.v1.context.add_async.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add_async = response.parse()
        assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: AlchemystAI) -> None:
        with client.v1.context.add_async.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add_async = response.parse()
            assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: AlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.context.add_async.with_raw_response.cancel(
                "",
            )


class TestAsyncAddAsync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlchemystAI) -> None:
        add_async = await async_client.v1.context.add_async.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        )
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAlchemystAI) -> None:
        add_async = await async_client.v1.context.add_async.create(
            context_type="resource",
            documents=[{"content": "Customer asked about pricing for the Scale plan."}],
            scope="internal",
            source="support-inbox",
            metadata={
                "file_name": "support_thread_TCK-1234.txt",
                "file_size": 2048,
                "file_type": "text/plain",
                "group_name": ["support", "pricing"],
                "last_modified": "2025-01-10T12:34:56.000Z",
            },
        )
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.add_async.with_raw_response.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add_async = await response.parse()
        assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.add_async.with_streaming_response.create(
            context_type="resource",
            documents=[{}],
            scope="internal",
            source="support-inbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add_async = await response.parse()
            assert_matches_type(AddAsyncCreateResponse, add_async, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncAlchemystAI) -> None:
        add_async = await async_client.v1.context.add_async.cancel(
            "id",
        )
        assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncAlchemystAI) -> None:
        response = await async_client.v1.context.add_async.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add_async = await response.parse()
        assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncAlchemystAI) -> None:
        async with async_client.v1.context.add_async.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add_async = await response.parse()
            assert_matches_type(AddAsyncCancelResponse, add_async, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncAlchemystAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.context.add_async.with_raw_response.cancel(
                "",
            )
