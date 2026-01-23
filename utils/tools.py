from langchain.tools import tool
from utils.helpers import get_github_client, proccess_issues

@tool
def fetch_issues(query:str):
    client = get_github_client()
    issues = client.search_issues(query=query,sort='created',order='desc')
    print(f"Found {issues.totalCount} matching issues!")
    issues = proccess_issues(issues=issues)
    return issues

