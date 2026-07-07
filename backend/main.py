from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.database.database import Base, engine
from app.api.upload import router as upload_router

from app.api.documents import router as document_router
from app.api.stats import router as stats_router

app = FastAPI(
    title="AssistIQ API",
    version="1.0.0",
    description="AI Powered Customer Support Assistant"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(document_router)
app.include_router(stats_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AssistIQ API"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }