# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ViewRetrieveParams"]


class ViewRetrieveParams(TypedDict, total=False):
    file_name: str
    """Name of the file to retrieve context for"""

    magic_key: str
    """Magic key for context retrieval"""
