from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.retrieval_service import search_documents
from app.services.chat_service import generate_answer

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(request: ChatRequest):

    docs, sources = search_documents(request.question)

    context = "\n".join(docs)

    answer = generate_answer(context, request.question)

    return {
        "answer": answer,
        "sources": sources
    }