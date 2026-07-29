from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    category: str
    records: list[dict]
