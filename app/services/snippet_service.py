import redis
from config.settings import REDIS_URL
from .llm_integration import sanitize_code
from uuid import uuid4
import json
from datetime import datetime

redis_client = redis.Redis.from_url(REDIS_URL)

def store_snippet(code: str):
    snippet_id = str(uuid4())
    snippet = {
        "id": snippet_id,
        "code": sanitize_code(code),
        "created_at": datetime.now().isoformat()
    }
    redis_client.set(f"snippet:{snippet_id}", json.dumps(snippet))
    return snippet_id

def get_snippets():
    keys = redis_client.keys("snippet:*")
    snippets = [json.loads(redis_client.get(k)) for k in keys]
    return snippets

def delete_snippet(snippet_id: str):
    redis_client.delete(f"snippet:{snippet_id}")
