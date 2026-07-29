from state import AgentState
from tools import get_records_by_category


# Start Node
def query_records(state: AgentState) -> dict:
    print('Querying records...')

    category = state.get('category', '')
    records = get_records_by_category(category)
    
    return {
        'records': records
    }

# Success Node
def display_records(state: AgentState) -> dict:
    print('Displaying records...')

    records = state.get('records', [])
    
    for record in records:
        print(f"ID: {record['id']}, Category: {record['category']}, Amount: {record['amount']}")

    return {}

# Retry Node
def ask_for_category(state: AgentState) -> dict:
    print('No records found.')

    category = input('Please enter another category: ')
    
    return {
        'category': category,
        'records': []
    }