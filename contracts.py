from pydantic import BaseModel, Field
from typing import Literal

class RecordRequest(BaseModel):
    category: Literal[
        'payments',
        'loans',
        'deposits',
        'unknown',
    ] = Field(
        description=(
            'The requested financial record category.' 
            "Requests for unknown categories will be handled by the 'unknown' category."
        ),
    )

    limit: int | None = Field(
        default=None,
        description=(
            'Maximum number of records requested. '
            'Use None when the user requests all records.'
        ),
    )
