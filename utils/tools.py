from langchain.tools import tool
import io
import requests
from zipfile import ZipFile
from typing import List, Dict
from utils.parsers import parser1
from utils.helpers import get_github_client, get_llm, get_repo_from_url, proccess_issues
from utils.prompts import likelihood_score_prompt


@tool
def fetch_issues(query: str) -> Dict:
    """
    Searches GitHub for open, unassigned issues based on a specific query string.

    Use this tool after generating a precise query string. It returns a processed
    collection of issues including titles, descriptions, and metadata.

    Args:
        query: A valid GitHub search API query string (e.g., 'label:"good first issue" language:python').

    Returns:
        A dictionary containing a list of processed issue objects and total count.
    """
    try:
        client = get_github_client()
        issues = client.search_issues(query=query, sort="created", order="desc")
        print(f"Found {issues.totalCount} matching issues!")
        issues = proccess_issues(issues=issues)
        client.close()
        return issues
    except Exception as e:
        return {"error": str(e), "issues": []}


@tool
def generate_github_query(user_goal: str, user_stack: str) -> str:
    """
    Transforms a user's high-level goal and technical stack into a structured GitHub search query string.
    It is a mandatory step before calling the fetch_issues tool.

    Args:
        user_goal: The specific type of contribution the user wants to make (e.g., 'bug fixes', 'documentation').
        user_stack: The programming languages or frameworks the user is proficient in (e.g., 'Python, Flask').

    Returns:
        A raw GitHub search string formatted with filters like 'state:open', 'no:assignee', and 'language:'.
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
    llm = get_llm()
    response = llm.invoke(prompt)
    return response.content


@tool
def get_likelihood_score(skill_set: str, metadata: List[Dict]) -> int:
    """
    Evaluates the compatibility between a user's skills and a specific GitHub issue.

    This tool uses an LLM to calculate a numerical score (0-100) representing how
    likely the user is to successfully resolve the issue based on the provided
    issue metadata and their skill set.

    Args:
        skill_set: A string describing the user's technical expertise and experience level.
        metadata: A list of dictionaries containing issue details (title, body, labels).

    Returns:
        An integer from 0 to 100, where 100 indicates a perfect match.
    """
    llm = get_llm()
    chain = likelihood_score_prompt | llm | parser1
    response = chain.invoke({"skill_set": skill_set, "metadata": metadata})
    if response.scores:
        return int(sum(score.score for score in response.scores) / len(response.scores))
    return 0


@tool
def fetch_codebase(url: str):
    '''
    Fetch the codebase of any public github repository, helps in in-depth analysis of codebase when needed.
    :param url: the url of github repository.
    :type url: str
    '''
    try:
        repo =  get_repo_from_url(url)
        # Get the url for Zip file.
        archive_url = repo.get_archive_link("zipball")
        # Get the Zip in Memory Buffer
        response = requests.get(archive_url)

        # Extract
        with ZipFile(io.BytesIO(response.content)) as z:
            z.extractall("./codebases")

        print("Codebase extracted successfully!")
        return 'Success'
    except Exception as e:
        return f'Failure,Reason: {e}'


tools = [fetch_issues, generate_github_query, get_likelihood_score,fetch_codebase]
