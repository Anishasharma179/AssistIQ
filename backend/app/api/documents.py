from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/")
def get_documents():

    db: Session = SessionLocal()

    documents = db.query(Document).all()

    db.close()

    return documents