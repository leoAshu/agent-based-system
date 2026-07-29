from langgraph.types import interrupt
from langchain_ollama import ChatOllama

from state import AgentState
from tools import get_records_by_category

from utils import (
    section,
    success,
    bullet
)

model = ChatOllama(
    model='qwen3:8b',
    temperature=0
)

# Start Node - LLM based category extraction
def extract_category(state: AgentState) -> dict:
    prompt = f'''
    Extract the record category from the user's request.

    Available categories:
    - payments
    - loans
    - deposits

    Return exactly one category from the list above.
    Do not singularize, pluralize, rename, or explain it.

    User request:
    {state["user_request"]}
    '''

    response = model.invoke(prompt)
    category = response.content.strip()

    return {
        'category': category
    }

# Query Node
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

    new_request = interrupt({
        'message': f"No records found for '{category}' category",
    })
    
    return {
        'user_request': new_request,
        'records': []
    }
