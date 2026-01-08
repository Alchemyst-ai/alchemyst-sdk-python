# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["StatusListParams"]


class StatusListParams(TypedDict, total=False):
    limit: str
    """Maximum number of jobs to return"""

    offset: str
    """Number of jobs to skip before starting to collect the result set"""

    type: Literal["all", "active", "failed", "completed"]
    """Type of jobs to list"""
