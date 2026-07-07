from app.services.vector_store import collection
from app.services.embedding_service import embedding_model


def retrieve_context(query: str, top_k: int = 4):

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

print("Retrieved documents:", documents)
print("Retrieved metadata:", metadatas)

    return documents, metadatas