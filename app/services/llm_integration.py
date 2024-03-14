import re
import redis
from openai import OpenAI
from config.settings import REDIS_URL, OPENAI_API_KEY
#========================================================================================================================================================================================================================================================================================================================
# Initialize Redis client
redis_client = redis.Redis.from_url(REDIS_URL)
#========================================================================================================================================================================================================================================================================================================================
# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)
#========================================================================================================================================================================================================================================================================================================================
def generate_code_with_feedback(description: str):
    # Retrieve global feedback
    feedback = redis_client.get("global_feedback")
    feedback_text = feedback.decode('utf-8') if feedback else ""
    if feedback_text:
        prompt = f"Task: {description}\nFeedback to consider: {feedback_text}\nGenerate a code snippet that fulfills the task description, taking into account the provided feedback. Ensure the code is clean, well-commented, and adheres to best practices."
    else:
        prompt = f"Given the task: '{description}', generate a code snippet that fulfills these requirements. Ensure the code is clean, well-commented, and adheres to best practices."
    
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.5, 
        max_tokens=200  
    )
    return response.choices[0].text
#========================================================================================================================================================================================================================================================================================================================
def store_feedback(feedback: str):
    redis_client.set("global_feedback", feedback)
#========================================================================================================================================================================================================================================================================================================================
def validate_prompt(prompt: str) -> bool:
    keywords = ['function', 'variable', 'class', 'return', 'if', 'else', 'while', 'for', 'print', 'int', 'string', 'list', 'dict', 'array']
    return any(keyword in prompt.lower() for keyword in keywords)
#========================================================================================================================================================================================================================================================================================================================
def sanitize_code(code: str) -> str:
    sanitized_code = re.sub(r'<script.*?>.*?</script>', '', code, flags=re.DOTALL)
    sanitized_code = re.sub(r'<.*?>', '', sanitized_code)  # Remove any remaining HTML tags
    return sanitized_code
#========================================================================================================================================================================================================================================================================================================================
