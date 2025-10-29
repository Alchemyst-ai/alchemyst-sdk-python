# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MemoryUpdateParams", "Content"]


class MemoryUpdateParams(TypedDict, total=False):
    contents: Iterable[Content]
    """Array of updated content objects"""

    memory_id: Annotated[str, PropertyInfo(alias="memoryId")]
    """The ID of the memory to update"""


class ContentTyped(TypedDict, total=False):
    content: str


Content: TypeAlias = Union[ContentTyped, Dict[str, object]]
