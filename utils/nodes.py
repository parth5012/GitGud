from typing import Dict, List
from utils.helpers import get_llm
from utils.prompts import likelihood_score_prompt
from utils.parsers import parser1
from langchain_core.output_parsers import StrOutputParser


def get_likelihood_score(skill_set:str, metadata:List[Dict]) -> int:
    """Used to retrieve the likelihood score of the issue being solved by the user based on his skillset."""
    llm = get_llm()
    chain = likelihood_score_prompt | llm | parser1
    response = chain.invoke({"skill_set": skill_set, "metadata": metadata})
    return int(response)
