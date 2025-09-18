# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContextSearchParams"]


class ContextSearchParams(TypedDict, total=False):
    minimum_similarity_threshold: Required[float]
    """Minimum similarity threshold"""

    query: Required[str]
    """The search query used to search for context data"""

    similarity_threshold: Required[float]
    """Maximum similarity threshold (must be >= minimum_similarity_threshold)"""

    metadata: object
    """Additional metadata for the search"""

    scope: Literal["internal", "external"]
    """Search scope"""

    user_id: str
    """The ID of the user making the request"""
