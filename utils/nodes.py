from langgraph.prebuilt import ToolNode
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from utils.tools import tools
from utils.helpers import get_llm
from utils.states import CoreState
from utils.prompts import SYSTEM_PROMPT


def chat_node(state: CoreState):
    llm = get_llm()
    messages = state["messages"]
    prompted_messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    llm = llm.bind_tools(tools)
    response = llm.invoke(prompted_messages).content
    return {"messages": [response]}


tool_node = ToolNode(tools)
