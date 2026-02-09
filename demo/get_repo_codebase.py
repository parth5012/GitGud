import requests
import zipfile
import io
from github import Repository


repo = Repository()
# 1. Get the link from PyGithub (as shown before)
url = repo.get_archive_link("zipball")

# 2. Download it into memory
response = requests.get(url)

# 3. Extract it directly from the memory buffer
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall("./my_codebase")

print("Codebase extracted successfully!")