from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from state import AgentState
from nodes import (
    extract_request,
    handle_deposits,
    handle_loans,
    handle_payments,
    handle_transfer,
    handle_unknown,
    generate_response,
)
from routes import route_request

graph = StateGraph(AgentState)

graph.add_node('extract_request', extract_request)
graph.add_node('deposits', handle_deposits)
graph.add_node('loans', handle_loans)
graph.add_node('payments', handle_payments)
graph.add_node('transfer', handle_transfer)
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
graph.add_edge('transfer', END)
graph.add_edge('unknown', END)
graph.add_edge('generate_response', END)

checkpointer = InMemorySaver()
app = graph.compile(checkpointer=checkpointer)

if __name__ == '__main__':

    config = {
        'configurable': {
            'thread_id': 'session-1'
        }
    }

    result = app.invoke({
        'messages': [
            {
                'role': 'user',
                'content': 'Transfer $500 to Alice.'
            }
        ],
        'request': None,
        },
        config=config
    )

    while '__interrupt__' in result:
        print(result['__interrupt__'])

        result = app.invoke(
            Command(resume=False), 
            config=config
        )
        
    print(result['messages'][-1].content)

