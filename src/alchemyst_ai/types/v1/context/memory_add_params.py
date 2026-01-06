# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["MemoryAddParams", "Content", "ContentMetadata", "Metadata"]


class MemoryAddParams(TypedDict, total=False):
    contents: Required[Iterable[Content]]
    """Array of content objects with metadata"""

    memory_id: Required[Annotated[str, PropertyInfo(alias="memoryId")]]
    """The ID of the memory"""

    metadata: Metadata
    """Optional metadata with groupName defaulting to ["default"]"""


class ContentMetadataTyped(TypedDict, total=False):
    message_id: Required[Annotated[str, PropertyInfo(alias="messageId")]]
    """Unique message ID"""


ContentMetadata: TypeAlias = Union[ContentMetadataTyped, Dict[str, object]]


class ContentTyped(TypedDict, total=False):
    content: Required[str]
    """The content of the memory message"""

    metadata: Required[ContentMetadata]


Content: TypeAlias = Union[ContentTyped, Dict[str, object]]


class MetadataTyped(TypedDict, total=False):
    """Optional metadata with groupName defaulting to ["default"]"""

    group_name: Annotated[SequenceNotStr[str], PropertyInfo(alias="groupName")]
    """Group names for the memory context"""


Metadata: TypeAlias = Union[MetadataTyped, Dict[str, object]]
