from typing import Dict, List
from utils import tools
from utils.helpers import get_llm
from utils.prompts import likelihood_score_prompt
from utils.parsers import parser1
from utils.states import ChatState
from langgraph.prebuilt import ToolNode

llm = get_llm()

def get_likelihood_score(skill_set: str, metadata: List[Dict]) -> int:
    """Used to retrieve the likelihood score of the issue being solved by the user based on his skillset."""
    chain = likelihood_score_prompt | llm | parser1
    response = chain.invoke({"skill_set": skill_set, "metadata": metadata})
    return int(response)


def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)