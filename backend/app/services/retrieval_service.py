from app.services.vector_store import collection
from app.services.embedding_service import embedding_model


def search_documents(query):

    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    documents = []
    sources = []

    if results["documents"]:
        documents = results["documents"][0]

    if results["metadatas"]:
        sources = [
            item["source"]
            for item in results["metadatas"][0]
        ]

    return documents, sources