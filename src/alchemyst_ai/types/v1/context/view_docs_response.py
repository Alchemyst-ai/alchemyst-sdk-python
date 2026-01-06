# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ViewDocsResponse", "Document"]


class Document(BaseModel):
    file_name: str = FieldInfo(alias="fileName")
    """Name of the file"""

    file_size: float = FieldInfo(alias="fileSize")
    """Size of the file in bytes"""

    file_type: str = FieldInfo(alias="fileType")
    """Type/MIME of the file"""

    group_name: List[str] = FieldInfo(alias="groupName")
    """Array of group names to which the file belongs"""

    last_modified: str = FieldInfo(alias="lastModified")
    """Last modified timestamp (ISO format)"""


class ViewDocsResponse(BaseModel):
    documents: List[Document]
