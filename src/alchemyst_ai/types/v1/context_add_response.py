# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContextAddResponse"]


class ContextAddResponse(BaseModel):
    context_id: str

    success: bool

    processed_documents: Optional[float] = None
