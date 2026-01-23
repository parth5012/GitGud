from langchain_core.prompts import PromptTemplate

likelihood_score_prompt = PromptTemplate.from_template("""You are an open source expert and your job is to evaluate the likelihood score of an issue to be solved by a user based on the given user's skill set and issue description.
                                                       Score should be an integer between 1 and 10.
## USER's SkillSet
{skill_set}
                                                       
## Issue Description
{description}.""")
