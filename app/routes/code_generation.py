from fastapi.responses import FileResponse
from fastapi import APIRouter, HTTPException
from ..models import CodeRequest, FeedbackRequest, CodeSnippet
from ..services.snippet_service import store_snippet, get_snippets, delete_snippet
from ..services.llm_integration import generate_code_with_feedback, store_feedback, validate_prompt, sanitize_code
from typing import List
#============================================================================================================================================================
router = APIRouter()
#============================================================================================================================================================
@router.get("/")
async def read_index():
    return FileResponse('app/templates/index.html')
#============================================================================================================================================================
@router.post("/generate-code/")
async def generate_code(request: CodeRequest):
    # Validate the prompt first
    if not validate_prompt(request.description):
        raise HTTPException(status_code=400, detail="Invalid prompt. Please ensure it's related to coding.")
    try:
        code = generate_code_with_feedback(request.description)
        # Sanitize the generated code before storing or returning it
        sanitized_code = sanitize_code(code)
        # Store the sanitized code snippet and get its ID
        snippet_id = store_snippet(sanitized_code)
        return {"code": sanitized_code, "snippet_id": snippet_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#============================================================================================================================================================
@router.post("/submit-feedback/")
async def submit_feedback(feedback: FeedbackRequest):
    try:
        store_feedback(feedback.feedback)
        return {"message": "Feedback received", "feedback": feedback.feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#============================================================================================================================================================
@router.get("/snippets/", response_model=List[CodeSnippet])
async def list_snippets():
    return get_snippets()
#============================================================================================================================================================
@router.delete("/snippets/{snippet_id}")
async def remove_snippet(snippet_id: str):
    delete_snippet(snippet_id)
    return {"message": "Snippet deleted successfully"}
#============================================================================================================================================================