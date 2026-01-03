# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["MemoryAddResponse"]


class MemoryAddResponse(BaseModel):
    context_id: str

    success: bool

    processed_documents: Optional[float] = None
