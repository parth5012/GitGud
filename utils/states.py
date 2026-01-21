from typing import Dict, TypedDict,List

class FilterAgentState(TypedDict):
    pass


class CoreState(TypedDict):
    skillset:str
    repo_url : str
    issues: List[Dict]
    
