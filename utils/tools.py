from langchain.tools import tool
from typing import List,Dict
from utils.parsers import parser1
from utils.helpers import get_github_client, get_llm, proccess_issues
from utils.prompts import likelihood_score_prompt


@tool
def fetch_issues(query:str) -> Dict:
    '''Fetch issues from github using the query given in input.'''
    client = get_github_client()
    issues = client.search_issues(query=query,sort='created',order='desc')
    print(f"Found {issues.totalCount} matching issues!")
    issues = proccess_issues(issues=issues)
    return issues

@tool
def generate_github_query(user_goal:str, user_stack: str) -> str:
    """
    Uses the LLM to convert user intent into a precise GitHub search query.
    """
    
    prompt = f"""
    You are an expert GitHub Scout. Your job is to create the PERFECT GitHub search query string.
    
    User Goal: {user_goal}
    User Tech Stack: {user_stack}
    
    Rules for the query:
    1. Always filter for 'state:open'.
    2. Always filter for 'no:assignee' (we want available issues).
    3. Use 'language:X' based on the stack.
    4. If they want beginner issues, use label:"good first issue" OR label:"help wanted".
    5. Return ONLY the raw query string. No markdown, no explanations.
    """
    llm =  get_llm()
    response = llm.invoke(prompt)
    return response

@tool
def get_likelihood_score(skill_set: str, metadata: List[Dict]) -> int:
    """Used to retrieve the likelihood score of the issue being solved by the user based on his skillset."""
    llm = get_llm()
    chain = likelihood_score_prompt | llm | parser1
    response = chain.invoke({"skill_set": skill_set, "metadata": metadata})
    return int(response)


tools = [fetch_issues,generate_github_query,get_likelihood_score]