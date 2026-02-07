from utils.tools import tools
from utils.helpers import get_llm
from utils.states import CoreState
from utils.prompts import chat_prompt
from langgraph.prebuilt import ToolNode
from langchain_core.output_parsers import StrOutputParser


def chat_node(state: CoreState):
    llm = get_llm()
    messages = state["messages"]
    chain =  chat_prompt | llm | StrOutputParser()
    response = chain.invoke(messages)
    return {"messages": [response]}


tool_node = ToolNode(tools)
