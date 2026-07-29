from langchain.tools import tool

from data import RECORDS

def get_records_by_category(category: str) -> list:
    """Retrieve all records belonging to the specified category."""
    normalized_category = category.strip().lower()

    return [
        record 
        for record in RECORDS 
        if record['category'] == normalized_category
    ]

@tool
def get_payments() -> list:
    """Retrieve all payment records."""
    return get_records_by_category('payments')

@tool
def get_loans() -> list:
    """Retrieve all loan records."""
    return get_records_by_category('loans')

@tool
def get_deposits() -> list:
    """Retrieve all deposit records."""
    return get_records_by_category('deposits')

