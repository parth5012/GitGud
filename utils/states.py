from typing import Dict, TypedDict,List, Annotated
from langgraph.graph.message import add_messages,BaseMessage


class FilterAgentState(TypedDict):
    pass


class CoreState(TypedDict):
    skillset:str
    issues: List[Dict]
    metadata: List[Dict]
    messages: Annotated[list[BaseMessage], add_messages]


