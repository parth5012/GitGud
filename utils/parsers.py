from langchain_core.output_parsers import PydanticOutputParser
from utils.models import ScoredIssueList


parser1 = PydanticOutputParser(pydantic_object=ScoredIssueList)