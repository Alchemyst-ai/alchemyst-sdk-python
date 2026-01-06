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

    metadata: Literal["true", "false"]
    """Controls whether metadata is included in the response:

    - metadata=true → metadata will be included in each context item in the
      response.
    - metadata=false (or omitted) → metadata will be excluded from the response for
      better performance.
    """

    mode: Literal["fast", "standard"]
    """Controls the search mode:

    - mode=fast → prioritizes speed over completeness.
    - mode=standard → performs a comprehensive search (default if omitted).
    """

    body_metadata: object
    """Additional metadata for the search"""

    scope: Literal["internal", "external"]
    """Search scope"""

    user_id: str
    """The ID of the user making the request"""
