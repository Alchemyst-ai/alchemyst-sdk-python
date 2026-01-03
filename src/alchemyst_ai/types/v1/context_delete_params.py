# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContextDeleteParams"]


class ContextDeleteParams(TypedDict, total=False):
    organization_id: Required[str]
    """Organization ID"""

    source: Required[str]
    """Source identifier for the context"""

    by_doc: Optional[bool]
    """Flag to delete by document"""

    by_id: Optional[bool]
    """Flag to delete by ID"""

    user_id: Optional[str]
    """Optional user ID"""
