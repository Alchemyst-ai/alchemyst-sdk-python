# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContextSearchResponse", "Context"]


class Context(BaseModel):
    content: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    metadata: Optional[object] = None

    score: Optional[float] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class ContextSearchResponse(BaseModel):
    contexts: Optional[List[Context]] = None
