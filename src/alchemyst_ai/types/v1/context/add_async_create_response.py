# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AddAsyncCreateResponse"]


class AddAsyncCreateResponse(BaseModel):
    job_id: str = FieldInfo(alias="jobId")

    queued: bool
