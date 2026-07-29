import json

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from state import AgentState
from routes import route_after_query
from nodes import (
    extract_category, 
    query_records, 
    display_records, 
    ask_for_category
)
    

from utils import (
    header,
    subheader,
    error,
    divider
)

graph = StateGraph(AgentState)

graph.add_node('extract_category', extract_category)
graph.add_node('query_records', query_records)
graph.add_node('display_records', display_records)
graph.add_node('ask_for_category', ask_for_category)

graph.add_edge(START, 'extract_category')
graph.add_edge('extract_category', 'query_records')
graph.add_conditional_edges(
    'query_records',
    route_after_query,
    {
        'success': 'display_records',
        'retry': 'ask_for_category'
    }
)
graph.add_edge('display_records', END)
graph.add_edge('ask_for_category', 'extract_category')

checkpointer = InMemorySaver()
app = graph.compile(checkpointer=checkpointer)

if __name__ == '__main__':
    header('Agent-Based System: Query Records by Category')

    request = input('What category of records do you want me to pull?: ')
    initial_state = {
        'user_request': request,
        'category': '',
        'records': []
    }
    
    config = {
        'configurable': {
            'thread_id': 'thread-1',
        }
    }


    result = app.invoke(initial_state, config=config)
    while '__interrupt__' in result:
        error(result['__interrupt__'][0].value['message'])
        divider()
        
        request = input('Please provide a new request:')

        result = app.invoke(
            Command(resume=request), 
            config=config
        )


    subheader('Final State')
    print(json.dumps(result, indent=2))
    divider()
