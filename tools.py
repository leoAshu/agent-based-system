from data import RECORDS

def get_records_by_category(category: str) -> list:
    normalized_category = category.strip().lower()

    return [
        record 
        for record in RECORDS 
        if record['category'] == normalized_category
    ]

def get_payments() -> list:
    return get_records_by_category('payments')

def get_loans() -> list:
    return get_records_by_category('loans')

def get_deposits() -> list:
    return get_records_by_category('deposits')