# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContextDeleteParams"]


class ContextDeleteParams(TypedDict, total=False):
    by_doc: Optional[bool]
    """Flag to delete by document"""

    by_id: Optional[bool]
    """Flag to delete by ID"""

    organization_id: Optional[str]
    """Optional organization ID"""

    source: str
    """Source identifier for the context"""

    user_id: Optional[str]
    """Optional user ID"""
