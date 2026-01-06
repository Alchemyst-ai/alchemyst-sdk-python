# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TraceListResponse", "Pagination", "Trace"]


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    has_prev_page: bool = FieldInfo(alias="hasPrevPage")

    limit: int

    page: int

    total: int

    total_pages: int = FieldInfo(alias="totalPages")


class Trace(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    created_at: datetime = FieldInfo(alias="createdAt")

    data: object

    organization_id: str = FieldInfo(alias="organizationId")

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")


class TraceListResponse(BaseModel):
    pagination: Pagination

    traces: List[Trace]
