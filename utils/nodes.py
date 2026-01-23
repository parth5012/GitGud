from utils.helpers import get_llm
from utils.prompts import likelihood_score_prompt
from langchain_core.output_parsers import StrOutputParser


def get_likelihood_score(skill_set:str, description:str) -> int:
    """Used to retrieve the likelihood score of the issue being solved by the user based on his skillset."""
    llm = get_llm()
    chain = likelihood_score_prompt | llm | StrOutputParser()
    response = chain.invoke({"skill_set": skill_set, "description": description})
    return int(response)
