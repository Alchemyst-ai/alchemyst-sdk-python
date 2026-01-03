# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MemoryAddParams", "Content"]


class MemoryAddParams(TypedDict, total=False):
    contents: Required[Iterable[Content]]
    """Array of content objects with additional properties allowed"""

    memory_id: Required[Annotated[str, PropertyInfo(alias="memoryId")]]
    """The ID of the memory"""


class ContentTyped(TypedDict, total=False):
    id: str
    """Unique message ID"""

    content: str
    """The content of the memory message"""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """Creation timestamp"""

    metadata: Dict[str, object]
    """Additional metadata for the message"""

    role: str
    """Role of the message sender (e.g., user, assistant)"""


Content: TypeAlias = Union[ContentTyped, Dict[str, object]]
