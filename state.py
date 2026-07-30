from langgraph.graph import MessagesState

from contracts import RecordRequest

class AgentState(MessagesState):
    request: RecordRequest | None
