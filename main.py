from langgraph.graph import StateGraph, START, END

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

app = graph.compile()

if __name__ == '__main__':
    print('Starting the agent-based system...')

    category = input('Please enter a category to query records: ')
    initial_state = {
        'category': category,
        'records': []
    }

    result = app.invoke(initial_state)
    print('Final result:', result)
