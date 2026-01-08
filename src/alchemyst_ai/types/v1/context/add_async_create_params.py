# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AddAsyncCreateParams", "Document", "Metadata"]


class AddAsyncCreateParams(TypedDict, total=False):
    context_type: Required[Literal["resource", "conversation", "instruction"]]
    """Type of context being added"""

    documents: Required[Iterable[Document]]
    """Array of documents with content and additional metadata"""

    scope: Required[Literal["internal", "external"]]
    """Scope of the context"""

    source: Required[str]
    """The source of the context data"""

    metadata: Metadata
    """Additional metadata for the context"""


class DocumentTyped(TypedDict, total=False):
    content: str
    """The content of the document"""


Document: TypeAlias = Union[DocumentTyped, Dict[str, str]]


class Metadata(TypedDict, total=False):
    """Additional metadata for the context"""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Name of the file"""

    file_size: Annotated[float, PropertyInfo(alias="fileSize")]
    """Size of the file in bytes"""

    file_type: Annotated[str, PropertyInfo(alias="fileType")]
    """Type/MIME of the file"""

    group_name: Annotated[SequenceNotStr[str], PropertyInfo(alias="groupName")]
    """Array of Group Name to which the file belongs to"""

    last_modified: Annotated[str, PropertyInfo(alias="lastModified")]
    """Last modified timestamp"""
