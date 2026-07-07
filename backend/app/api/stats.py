from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document

router = APIRouter(
    prefix="/stats",
    tags=["Dashboard"]
)


@router.get("/")
def stats():

    db: Session = SessionLocal()

    total_documents = db.query(Document).count()

    db.close()

    estimated_chunks = total_documents * 4

    return {
        "documents": total_documents,
        "chunks": estimated_chunks,
        "questions": 0,
        "status": "Active"
    }