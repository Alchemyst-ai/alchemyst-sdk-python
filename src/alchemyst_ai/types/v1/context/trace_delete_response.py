# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TraceDeleteResponse", "Trace", "TraceData"]


class TraceData(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    query: Optional[str] = None

    source: Optional[str] = None


class Trace(BaseModel):
    """The deleted trace data"""

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    data: Optional[TraceData] = None

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    type: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class TraceDeleteResponse(BaseModel):
    trace: Trace
    """The deleted trace data"""
