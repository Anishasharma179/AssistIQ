import chromadb
from app.services.embedding_service import embedding_model

client = chromadb.PersistentClient(
    path="storage/chroma_new"
)

collection = client.get_or_create_collection(
    name="knowledge_base_new"
)


def add_chunks(chunks, filename):

    if not chunks:
        print("No chunks generated.")
        return

    embeddings = embedding_model.encode(chunks).tolist()

    ids = [f"{filename}_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"source": filename} for _ in chunks]
    )

    print(f"Stored {len(chunks)} chunks")
    print("Collection count:", collection.count())