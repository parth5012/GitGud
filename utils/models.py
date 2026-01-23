from pydantic import BaseModel,Field
from typing import List



# 1. Define the Schema for a single issue
class IssueScore(BaseModel):
    issue_id: str = Field(description="The URL or ID of the GitHub issue")
    score: int = Field(description="Likelihood score from 1-10", ge=1, le=10)
    reasoning: str = Field(description="One sentence explaining the score")
    priority_tag: str = Field(description="High Match, Stretch Goal, or Ignore")

# 2. Define the wrapper for a list of scores
class ScoredIssueList(BaseModel):
    scores: List[IssueScore]