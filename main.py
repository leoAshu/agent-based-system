from langgraph.graph import MessagesState, StateGraph, START
from langgraph.prebuilt import tools_condition

from nodes import call_model, tool_node

graph = StateGraph(MessagesState)

graph.add_node('call_model', call_model)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'call_model')
graph.add_conditional_edges(
    'call_model',
    tools_condition,
)
graph.add_edge('tools', 'call_model')

app = graph.compile()

result = app.invoke({
    'messages': [
        {
            'role': 'user',
            'content': 'Show me all payments.'
        }
    ]
})

for message in result['messages']:
    print(type(message).__name__)
    print(message.content)
    print()
