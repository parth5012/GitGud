from utils import tools
from utils.helpers import get_llm
from utils.states import ChatState
from langgraph.prebuilt import ToolNode

def chat_node(state: ChatState):
    llm = get_llm()
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)