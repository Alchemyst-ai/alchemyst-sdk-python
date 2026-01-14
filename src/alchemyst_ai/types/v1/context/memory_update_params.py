# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MemoryUpdateParams", "Content"]


class MemoryUpdateParams(TypedDict, total=False):
    contents: Required[Iterable[Content]]
    """Array of updated content objects"""

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """The ID of the memory to update"""


class Content(TypedDict, total=False):
    id: str
    """Unique ID for the message"""

    content: str
    """The content of the memory entry"""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """Creation timestamp"""

    metadata: Dict[str, object]
    """Additional metadata for the memory entry"""

    role: str
    """Role of the message (e.g., user, assistant)"""
