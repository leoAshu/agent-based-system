from pydantic import BaseModel, Field
from typing import Literal

class RecordRequest(BaseModel):
    category: Literal[
        'payments',
        'loans',
        'deposits',
        'transfer',
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
    recipient: str | None = Field(
        default=None,
        description=(
            'Name of the recipient receiving the money. '
            "For 'Transfer $500 to Alice', use 'Alice'. "
            'Only populate for transfer requests.'
        ),
    )
    amount: float | None = Field(
        default=None,
        description=(
            'Numeric amount to transfer, without a currency symbol. '
            "For 'Transfer $500 to Alice', use 500. "
            'Only populate for transfer requests.'
        ),
    )
