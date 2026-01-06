# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ViewRetrieveResponse", "Context", "ContextMetadata"]


class ContextMetadata(BaseModel):
    """Additional metadata for the context"""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)

    file_type: Optional[str] = FieldInfo(alias="fileType", default=None)

    group_name: Optional[List[str]] = FieldInfo(alias="groupName", default=None)

    last_modified: Optional[str] = FieldInfo(alias="lastModified", default=None)


class Context(BaseModel):
    content: Optional[str] = None
    """The content of the context item"""

    metadata: Optional[ContextMetadata] = None
    """Additional metadata for the context"""


class ViewRetrieveResponse(BaseModel):
    contexts: List[Context]
    """List of context items"""

    success: bool
