from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=50
)


def split_text(text: str):
    return splitter.split_text(text)