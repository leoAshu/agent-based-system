from typing import TypedDict

class AgentState(TypedDict):
    category: str
    records: list[dict]

