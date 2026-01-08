# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["StatusListResponse", "Job"]


class Job(BaseModel):
    attempts_made: float = FieldInfo(alias="attemptsMade")

    data: object

    job_id: str = FieldInfo(alias="jobId")

    status: str

    failed_reason: Optional[str] = FieldInfo(alias="failedReason", default=None)

    finished_on: Optional[float] = FieldInfo(alias="finishedOn", default=None)

    processed_on: Optional[float] = FieldInfo(alias="processedOn", default=None)


class StatusListResponse(BaseModel):
    jobs: List[Job]

    success: bool
