from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from github import Github




load_dotenv()


def create_embeddings():
    pass

def store_embeddings():
    pass

def get_llm() -> ChatGoogleGenerativeAI:
    api_key = os.getenv('GOOGLE_API_KEY')
    return ChatGoogleGenerativeAI(model = 'gemini-2.5-flash',api_key=api_key)

def get_github_client() -> Github:
    access_token = os.getenv('GITHUB_TOKEN')
    client = Github(access_token)
    return client

def proccess_issues(issues):
    
    issue_data = []
    for issue in issues[:10]:  # Limit to top 10 for analysis
        repo = issue.repository
        
        # Metadata for your LangGraph "Filter Agent"
        issue_data += {
            "title": issue.title,
            "url": issue.html_url,
            "repo_name": repo.full_name,
            "stars": repo.stargazers_count,
            "labels": [label.name for label in issue.labels],
            "created_at": issue.created_at,
            "comments_count": issue.comments
        }
        
    print(f"[{issue_data['repo_name']}] {issue_data['title']}")

    return issue_data
