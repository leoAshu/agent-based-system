from langchain_ollama import ChatOllama
from langchain_core.messages import ToolMessage

from contracts import RecordRequest
from state import AgentState
from tools import (
    get_deposits,
    get_loans,
    get_payments
)

model = ChatOllama(
    model='qwen3:8b',
    temperature=0
)

structured_model = model.with_structured_output(RecordRequest)

def extract_request(state: AgentState) -> dict:
    user_message = state['messages'][-1]

    request = structured_model.invoke(user_message.content)

    return {
        'request': request
    }

def handle_payments(state: AgentState) -> dict:
    data = get_payments.invoke({})
    message = ToolMessage(
        content=str(data),
        tool_call_id='get_payments'
    )

    return {
        'messages': [message]
    }

def handle_loans(state: AgentState) -> dict:
    data = get_loans.invoke({})
    message = ToolMessage(
        content=str(data),
        tool_call_id='get_loans'
    )

    return {
        'messages': [message]
    }

def handle_deposits(state: AgentState) -> dict:
    data = get_deposits.invoke({})
    message = ToolMessage(
        content=str(data),
        tool_call_id='get_deposits'
    )

    return {
        'messages': [message]
    }

def handle_unknown(state: AgentState) -> dict:
    pmessage = ToolMessage(
        content='Unknown category. Please specify payments, loans, or deposits.',
        tool_call_id='get_unknown'
    )

def generate_response(state: AgentState) -> dict:
    messages = state['messages']
    response = model.invoke(messages)

    return {
        'messages': [response]
    }
