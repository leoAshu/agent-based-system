from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes import (
    extract_request,
    handle_deposits,
    handle_loans,
    handle_payments,
    handle_unknown,
    generate_response
)
from routes import route_request

graph = StateGraph(AgentState)

graph.add_node('extract_request', extract_request)
graph.add_node('deposits', handle_deposits)
graph.add_node('loans', handle_loans)
graph.add_node('payments', handle_payments)
graph.add_node('unknown', handle_unknown)
graph.add_node('generate_response', generate_response)


graph.add_edge(START, 'extract_request')
graph.add_conditional_edges(
    'extract_request',
    route_request,
)
graph.add_edge('deposits', 'generate_response')
graph.add_edge('loans', 'generate_response')
graph.add_edge('payments', 'generate_response')
graph.add_edge('unknown', END)
graph.add_edge('generate_response', END)

app = graph.compile()

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Show me all payments."
        }
    ],
    "request": None,
})

for message in result['messages']:
    print(type(message).__name__)
    print(message.content)
    print()

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Display my loan transactions."
        }
    ],
    "request": None,
})

for message in result['messages']:
    print(type(message).__name__)
    print(message.content)
    print()

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Show money credited into my account."
        }
    ],
    "request": None,
})

for message in result['messages']:
    print(type(message).__name__)
    print(message.content)
    print()

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Show me all the heroes."
        }
    ],
    "request": None,
})

for message in result['messages']:
    print(type(message).__name__)
    print(message.content)
    print()
