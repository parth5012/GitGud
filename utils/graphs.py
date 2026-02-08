from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition
from utils.nodes import chat_node, tool_node
from .states import CoreState, FilterAgentState


def get_filter_agent():
    """
    Used for Filtering out Open Source repos based on metrics like Star to Issues Ratio,Maintainer Responsiveness and Issue difficulty.
    """
    graph = StateGraph(state_schema=FilterAgentState)


def get_semantic_matcher():
    """
    Used to match the given skillset with the selected issue.
    """
    pass


def build_core_graph():
    graph = StateGraph(state_schema=CoreState)
    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    graph.set_entry_point("chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    workflow = graph.compile()
    return workflow
