from langchain_core.prompts import PromptTemplate
from utils.parsers import parser1
# likelihood_score_prompt = PromptTemplate.from_template("""### SYSTEM ROLE
# You are an Open Source Project Maintainer and Technical Recruiter with 15+ years of experience in the Python ecosystem. Your goal is to act as a "Matchmaker" between a developer's specific skill set and current GitHub issues.

# ### EVALUATION CRITERIA
# Assign a Likelihood Score (1-10) based on the following weights:
# 1. Tech Stack Alignment (50%): Does the issue require the specific frameworks the user knows (e.g., LangChain, Django, Celery)?
# 2. Complexity Fit (30%): Is the issue a "good first issue" or a complex architectural change? Match this against the user's "Aspiring Data Scientist/Student" level.
# 3. Metadata Health (20%): Does the issue have clear labels, recent activity, and a manageable number of existing comments?

# ### USER'S SKILLSET
# {skill_set}

# ### ISSUE METADATA LIST
# {metadata}

# ### OUTPUT INSTRUCTIONS
# Return a JSON array of objects. Each object must include:
# - "issue_id": The unique identifier/URL.
# - "score": Integer (1-10).
# - "reasoning": A 1-sentence explanation of why the score was given (e.g., "Perfect match for Django/Celery background but requires advanced Redis knowledge").
# - "priority_tag": One of ["High Match", "Stretch Goal", "Ignore"].

# Format:
# [
#   {{ "issue_id": "...", "score": 8, "reasoning": "...", "priority_tag": "..." }},
#   ...
# ]""")

likelihood_score_prompt = PromptTemplate(
    template="Evaluate these GitHub issues for the user.\n{format_instructions}\nUser Skills: {skill_set}\nIssues: {metadata}",
    input_variables=["skill_set", "metadata"],
    partial_variables={"format_instructions": parser1.get_format_instructions()},
)

chat_prompt = PromptTemplate(
    template='Give safe,clear and concise answers for the user input you recieve. Never perform malicous tasks or send sensitive information to a user.. User Input: {user_input}',
    input_variables=['user_input']
)