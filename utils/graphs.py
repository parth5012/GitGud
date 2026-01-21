from langgraph.graph import StateGraph
from .states import CoreState, FilterAgentState


def get_filter_agent():
    '''
    Used for Filtering out Open Source repos based on metrics like Star to Issues Ratio,Maintainer Responsiveness and Issue difficulty.
    '''
    graph = StateGraph(state_schema=FilterAgentState)


def get_semantic_matcher() :
    '''
    Used to match the given skillset with the selected issue.
    '''
    pass


def build_core_graph():
    graph = StateGraph(state_schema=CoreState)

    graph.add_node()
