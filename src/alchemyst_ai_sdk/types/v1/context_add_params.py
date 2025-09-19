# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContextAddParams", "Document", "Metadata"]


class ContextAddParams(TypedDict, total=False):
    context_type: Literal["resource", "conversation", "instruction"]
    """Type of context being added"""

    documents: Iterable[Document]
    """Array of documents with content and additional metadata"""

    metadata: Metadata
    """Additional metadata for the context"""

    scope: Literal["internal", "external"]
    """Scope of the context"""

    source: str
    """The source of the context data"""


class DocumentTyped(TypedDict, total=False):
    content: str
    """The content of the document"""


Document: TypeAlias = Union[DocumentTyped, Dict[str, str]]


class Metadata(TypedDict, total=False):
    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Name of the file"""

    file_size: Annotated[float, PropertyInfo(alias="fileSize")]
    """Size of the file in bytes"""

    file_type: Annotated[str, PropertyInfo(alias="fileType")]
    """Type/MIME of the file"""

    last_modified: Annotated[str, PropertyInfo(alias="lastModified")]
    """Last modified timestamp"""
