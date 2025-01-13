from typing import List, Dict, Any
from pydantic import BaseModel
import json
from prompts.prompt_loader import load_prompt
from modules.openai_with_gemini import openai_client

class ResultRelevance(BaseModel):
    explanation: str
    id: str

class RelevanceCheckOutput(BaseModel):
    relevant_results: List[ResultRelevance]
    
def check_search_relevance(search_results: Dict[str, Any], prompt: str) -> RelevanceCheckOutput:
    """
    Analyze search results and determine the most relevant ones.

    Args:
        search_results: Dictionary containing search results to analyze
    
    Returns:
        RelevanceCheckOutput containing the most relevant results and explanation
    """
   
    # print(f" search_result {search_results}")
    completion = openai_client.beta.chat.completions.parse(
    model="gemini-1.5-flash",
    messages=[
        {"role": "system", "content": f"{prompt}"},
        {"role": "user", "content": f"{search_results}"},
    ],
    response_format=RelevanceCheckOutput,)
    # print(completion.choices[0].message.parsed)
    # print(f"Gemini response after processing search_results {completion.choices[0].message.content}")
    # Access the list of relevant results
    selected_by_llm = completion.choices[0].message.content
    results = json.loads(selected_by_llm) 

    return results
