import os

from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.document import Document
from app.services.file_service import save_file
from app.services.document_parser import extract_text
from app.services.text_splitter import split_text
from app.services.vector_store import add_chunks

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

ALLOWED_EXTENSIONS = [".pdf", ".docx", ".txt"]


@router.post("/")
def upload_document(file: UploadFile = File(...)):
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are allowed."
        )

    filename, file_path = save_file(file)

    text = extract_text(file_path)

    chunks = split_text(text)

    add_chunks(chunks, filename)

    db: Session = SessionLocal()

    document = Document(
        filename=filename,
        filetype=extension
    )

    db.add(document)
    db.commit()
    db.refresh(document)
    db.close()

    return {
        "message": "Document uploaded successfully",
        "document": {
            "id": document.id,
            "filename": document.filename,
            "filetype": document.filetype
        }
    }