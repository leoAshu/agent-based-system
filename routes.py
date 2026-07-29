from state import AgentState

def route_after_query(state: AgentState) -> str:
    records = state.get('records', [])
    
    return 'success' if records else 'retry'
