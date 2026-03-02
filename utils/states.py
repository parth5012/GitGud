from typing import Dict, TypedDict,List, Annotated
from langgraph.graph.message import add_messages,BaseMessage
import operator

class FilterAgentState(TypedDict):
    pass


class CoreState(TypedDict):
    issues: List[Dict]
    scored_issues: Annotated[List[Dict],operator.add]
    metadata: List[Dict]
    messages: Annotated[list[BaseMessage], add_messages]
    final_response: str
    query: str
    user_goal: str
    user_stack: str
    error: str  

