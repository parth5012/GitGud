from utils.tools import tools
from utils.helpers import get_llm
from utils.states import CoreState
from langgraph.prebuilt import ToolNode

def chat_node(state: CoreState):
    llm = get_llm()
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)