from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    filetype: str

    class Config:
        from_attributes = True