# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TraceListResponse", "Trace"]


class Trace(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    data: Optional[object] = None

    type: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class TraceListResponse(BaseModel):
    traces: Optional[List[Trace]] = None
