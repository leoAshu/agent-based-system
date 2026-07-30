from state import AgentState

def route_request(state: AgentState) -> dict:
    request = state['request']

    return request.category
