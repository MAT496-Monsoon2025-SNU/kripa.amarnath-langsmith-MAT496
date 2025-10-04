from pydantic import BaseModel, Field
from groq import Groq
import os

# Assuming you've set your Groq API key in your environment variables
# For example: export GROQ_API_KEY="gsk_..."
# Or load from .env if you prefer:
# from dotenv import load_dotenv
# load_dotenv(dotenv_path="../../.env", override=True)

class Similarity_Score(BaseModel):
    similarity_score: int = Field(description="Semantic similarity score between 1 and 10, where 1 means unrelated and 10 means identical.")

def compare_semantic_similarity_groq(input_question: str, reference_response: str, run_response: str):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY") or "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")

    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a semantic similarity evaluator. Compare the meanings of two responses to a question, "
                    "Reference Response and New Response, where the reference is the correct answer, and we are trying to judge if the new response is similar. "
                    "Provide a score between 1 and 10, where 1 means completely unrelated, and 10 means identical in meaning. "
                    "Respond ONLY with a JSON object containing a 'similarity_score' integer."
                ),
            },
            {"role": "user", "content": f"Question: {input_question}\n Reference Response: {reference_response}\n Run Response: {run_response}"}
        ],
        response_format={"type": "json_object"},
    )

    # Manually parse the JSON since client.beta.chat.completions.parse is an OpenAI specific feature
    import json
    parsed_response = json.loads(completion.choices[0].message.content)
    similarity_score_model = Similarity_Score(**parsed_response)
    return similarity_score_model.similarity_score