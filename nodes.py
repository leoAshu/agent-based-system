from langgraph.graph import MessagesState
from langchain_ollama import ChatOllama
from langgraph.prebuilt import ToolNode

from tools import (
    get_deposits,
    get_loans,
    get_payments
)

model = ChatOllama(
    model='qwen3:8b',
    temperature=0
)

llm_with_tools = model.bind_tools([
    get_deposits,
    get_loans,
    get_payments
])

def call_model(state: MessagesState) -> dict:
    messages = state['messages']
    response = llm_with_tools.invoke(messages)

    return {
        'messages': [response]
    }

tools = [
    get_deposits,
    get_loans,
    get_payments
]

tool_node = ToolNode(tools)
