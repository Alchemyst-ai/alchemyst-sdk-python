# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["MemoryUpdateResponse"]


class MemoryUpdateResponse(BaseModel):
    memory_id: str

    success: bool

    updated_entries: float
