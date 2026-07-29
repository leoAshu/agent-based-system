from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from state import AgentState
from nodes import query_records, display_records, ask_for_category
from routes import route_after_query

graph = StateGraph(AgentState)

graph.add_node('query_records', query_records)
graph.add_node('display_records', display_records)
graph.add_node('ask_for_category', ask_for_category)

graph.add_edge(START, 'query_records')
graph.add_conditional_edges(
    'query_records',
    route_after_query,
    {
        'success': 'display_records',
        'retry': 'ask_for_category'
    }
)
graph.add_edge('display_records', END)
graph.add_edge('ask_for_category', 'query_records')

checkpointer = InMemorySaver()
app = graph.compile(checkpointer=checkpointer)

if __name__ == '__main__':
    print('Starting the agent-based system...')

    category = input('Please enter a category to query records: ')
    initial_state = {
        'category': category,
        'records': []
    }
    
    config = {
        'configurable': {
            'thread_id': 'thread-1',
        }
    }


    result = app.invoke(initial_state, config=config)
    while '__interrupt__' in result:
        print(result['__interrupt__'][0].value['message'])
        
        new_category = input('Please enter a new category: ')

        result = app.invoke(
            Command(resume=new_category), 
            config=config
        )



    print('Final result:', result)
