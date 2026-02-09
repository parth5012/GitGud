import random
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from github import Github
from github.Auth import Token
from langchain_groq import ChatGroq


load_dotenv()


def create_embeddings():
    pass


def store_embeddings():
    pass


def get_llm() -> ChatGoogleGenerativeAI:
    llm_choice = random.randint(0, 1)
    if llm_choice == 0:
        api_key = os.getenv("GOOGLE_API_KEY")
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)
    else:
        api_key = os.getenv("GROQ_API_KEY")
        return ChatGroq(model="qwen/qwen3-32b")


def get_github_client() -> Github:
    access_token = Token(os.getenv("GITHUB_TOKEN"))
    client = Github(auth=access_token)
    return client


def proccess_issues(issues):
    issue_data = []
    for issue in issues[:10]:
        repo = issue.repository

        issue_dict = {
            "title": issue.title,
            "url": issue.html_url,
            "repo_name": repo.full_name,
            "stars": repo.stargazers_count,
            "labels": [label.name for label in issue.labels],
            "created_at": issue.created_at,
            "comments_count": issue.comments,
        }

        issue_data.append(issue_dict)
        print(f"[{issue_dict['repo_name']}] {issue_dict['title']}")

    return issue_data
