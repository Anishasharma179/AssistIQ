from fastapi import APIRouter
from app.schemas.chat import ChatRequest

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(request: ChatRequest):

    question = request.question.lower()

    if "refund" in question:
        answer = "Refunds are processed within 7 business days."

    elif "password" in question or "forgot" in question:
        answer = 'Employees can reset their password by clicking "Forgot Password" on the login page.'

    elif "email" in question or "contact" in question or "support" in question:
        answer = "You can contact our support team at support@assistiq.com."

    elif "office" in question or "time" in question or "timing" in question:
        answer = "Our office timings are Monday to Friday from 9:00 AM to 6:00 PM."

    else:
        answer = "Sorry, I couldn't find relevant information in the uploaded company documents."

    return {
        "answer": answer,
        "sources": ["company.txt"]
    }