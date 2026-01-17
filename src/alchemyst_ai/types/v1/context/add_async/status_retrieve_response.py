# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["StatusRetrieveResponse"]


class StatusRetrieveResponse(BaseModel):
    job_id: str = FieldInfo(alias="jobId")

    status: str

    success: bool

    attempts_made: Optional[float] = FieldInfo(alias="attemptsMade", default=None)

    failed_reason: Optional[str] = FieldInfo(alias="failedReason", default=None)

    finished_on: Optional[float] = FieldInfo(alias="finishedOn", default=None)

    processed_on: Optional[float] = FieldInfo(alias="processedOn", default=None)

    result: Optional[object] = None
    """Result of the job (if available)"""
