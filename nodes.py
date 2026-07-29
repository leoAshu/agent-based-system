from langgraph.types import interrupt

from state import AgentState
from tools import get_records_by_category

from utils import (
    section,
    success,
    bullet
)

# Start Node
def query_records(state: AgentState) -> dict:
    section('Querying records...')

    category = state.get('category', '')
    records = get_records_by_category(category)
    
    return {
        'records': records
    }

# Success Node
def display_records(state: AgentState) -> dict:
    success('Records found:')

    records = state.get('records', [])
    
    for record in records:
        bullet(f"ID: {record['id']}, Category: {record['category']}, Amount: {record['amount']}")

    return {}

# Retry Node
def ask_for_category(state: AgentState) -> dict:
    category = state.get('category', '')

    new_category = interrupt({
        'message': 'No records found.',
        'invalid_category': category,
    })
    
    return {
        'category': new_category,
        'records': []
    }
