# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["MemoryAddParams", "Content", "ContentMetadata", "Metadata"]


class MemoryAddParams(TypedDict, total=False):
    contents: Required[Iterable[Content]]
    """Array of content objects.

    Each object must contain at least the 'content' field. Additional properties are
    allowed.
    """

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """The ID of the session"""

    metadata: Metadata
    """Optional metadata for the memory context.

    Defaults to ["default"] if not provided.
    """


class ContentMetadata(TypedDict, total=False):
    """Additional metadata for the message (optional)"""

    message_id: Annotated[str, PropertyInfo(alias="messageId")]
    """Unique message ID"""


class ContentTyped(TypedDict, total=False):
    content: Required[str]
    """The content of the memory message"""

    metadata: ContentMetadata
    """Additional metadata for the message (optional)"""


Content: TypeAlias = Union[ContentTyped, Dict[str, object]]


class MetadataTyped(TypedDict, total=False):
    """Optional metadata for the memory context.

    Defaults to ["default"] if not provided.
    """

    group_name: Annotated[SequenceNotStr[str], PropertyInfo(alias="groupName")]
    """Optional group names for the memory context.

    Defaults to ["default"] if not provided.
    """


Metadata: TypeAlias = Union[MetadataTyped, Dict[str, object]]
