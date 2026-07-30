from langchain_ollama import ChatOllama
from langchain_core.messages import ToolMessage, HumanMessage, SystemMessage, AIMessage

from contracts import RecordRequest
from state import AgentState
from tools import (
    get_deposits,
    get_loans,
    get_payments
)
from prompts import CATEGORY_EXTRACTION_PROMPT

model = ChatOllama(
    model='qwen3:8b',
    temperature=0
)

structured_model = model.with_structured_output(RecordRequest)

def extract_request(state: AgentState) -> dict:
    user_message = state['messages'][-1]

    request_prompts = [
        SystemMessage(content=CATEGORY_EXTRACTION_PROMPT),
        HumanMessage(content=user_message.content)
    ]

    request = structured_model.invoke(request_prompts)

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
    return {
        "messages": [
            AIMessage(
                content=(
                    "I can only help with payments, loans, and deposits."
                )
            )
        ]
    }

def generate_response(state: AgentState) -> dict:
    messages = state['messages']
    response = model.invoke(messages)

    return {
        'messages': [response]
    }
