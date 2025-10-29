# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MemoryDeleteParams"]


class MemoryDeleteParams(TypedDict, total=False):
    memory_id: Annotated[str, PropertyInfo(alias="memoryId")]
    """The ID of the memory to delete"""

    organization_id: Optional[str]
    """Optional organization ID"""

    user_id: Optional[str]
    """Optional user ID"""
