from pypdf import PdfReader
from docx import Document


def read_pdf(file_path: str):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file_path: str):
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def read_txt(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_text(file_path: str):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)

    if file_path.endswith(".docx"):
        return read_docx(file_path)

    if file_path.endswith(".txt"):
        return read_txt(file_path)

    return ""