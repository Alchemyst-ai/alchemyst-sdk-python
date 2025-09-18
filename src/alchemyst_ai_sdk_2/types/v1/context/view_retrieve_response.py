# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ViewRetrieveResponse"]


class ViewRetrieveResponse(BaseModel):
    context: Optional[List[object]] = None
    """List of context items"""
