# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TraceListParams"]


class TraceListParams(TypedDict, total=False):
    limit: int
    """Number of traces per page"""

    page: int
    """Page number for pagination"""
