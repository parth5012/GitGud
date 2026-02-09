import requests
import zipfile
import os
import io
from github import Github
from github.Auth import Token

access_token = os.getenv("GITHUB_TOKEN")
token = Token(access_token)
g = Github(auth=token)

repo = g.get_repo("githubtraining/hellogitworld")
# 1. Get the link from PyGithub (as shown before)
url = repo.get_archive_link("zipball")

# 2. Download it into memory
response = requests.get(url)

# 3. Extract it directly from the memory buffer
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall("./my_codebase")

print("Codebase extracted successfully!")
